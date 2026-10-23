"""Check raster pixels against the cropped, physical size used in the book.

PNG/JPEG headers suffice; normal publication builds need no imaging package.
"""
import struct


def raster_pixels(path):
    with path.open('rb') as stream:
        header = stream.read(24)
        if header.startswith(b'\x89PNG\r\n\x1a\n') and header[12:16] == b'IHDR':
            return struct.unpack('>II', header[16:24])
        stream.seek(0)
        if stream.read(2) != b'\xff\xd8':
            raise ValueError(f'Expected PNG or JPEG: {path}')
        while True:
            prefix = stream.read(1)
            if prefix != b'\xff':
                raise ValueError(f'Malformed JPEG header: {path}')
            marker = stream.read(1)
            while marker == b'\xff':
                marker = stream.read(1)
            if not marker or marker in (b'\xd9', b'\xda'):
                raise ValueError(f'JPEG has no frame size: {path}')
            if marker == b'\x01' or 0xd0 <= marker[0] <= 0xd7:
                continue
            length = struct.unpack('>H', stream.read(2))[0]
            if marker[0] in (0xc0, 0xc1, 0xc2, 0xc3, 0xc5, 0xc6, 0xc7, 0xc9, 0xca, 0xcb, 0xcd, 0xce, 0xcf):
                _, height, width = struct.unpack('>BHH', stream.read(5))
                return width, height
            stream.seek(length-2, 1)


def validate_layout(root, assets, publication, puzzles):
    layouts = publication['layout'].get('puzzle_layouts', {})
    minimum = publication['layout'].get('minimum_raster_ppi')
    if minimum is None:
        return
    figures = (root / assets / 'figures').resolve()
    bank = {p['id']: p for p in puzzles}
    modes = {'text-only', 'data-inline', 'side-left', 'side-right', 'wrap-left', 'wrap-right', 'banner-before', 'banner-after'}
    for pid, setting in layouts.items():
        if pid not in bank or setting.get('mode') not in modes:
            raise ValueError(f'Invalid illustration layout: {pid}')
        if setting['mode'] == 'text-only':
            if any(key in setting for key in ('raster_path', 'crop', 'model_kind')):
                raise ValueError(f'Text-only puzzle still selects an image: {pid}')
            continue
        if setting.get('model_kind') and 'raster_path' in setting:
            raise ValueError(f'Conflicting diagram and raster selections: {pid}')
        if setting['mode']=='data-inline' and ('{{DATA}}' not in bank[pid]['statement'] or not setting.get('model_kind')):
            raise ValueError(f'Inline diagram requires an input placeholder and model: {pid}')
        if setting['mode']=='data-inline' and (setting['model_kind']!='coin-row' or (bank[pid].get('instance') or {}).get('kind')!='end-coins'):
            raise ValueError(f'Inline diagram must preserve every input value: {pid}')
        if setting['mode'].startswith('wrap-') and '{{DATA}}' in bank[pid]['statement']:
            raise ValueError(f'Tables must not wrap around an image: {pid}')
        width_mm = setting.get('width_mm', 0)
        if not 30 <= width_mm <= 167:
            raise ValueError(f'Invalid physical figure width: {pid}')
        if 'raster_path' not in setting:
            continue
        path = (figures / setting['raster_path']).resolve()
        if not path.is_relative_to(figures.parent) or not path.is_file():
            raise ValueError(f'Invalid publication raster path: {pid}')
        if path.stem != bank[pid].get('figure_id'):
            raise ValueError(f'Publication raster does not match current figure: {pid}')
        crop = setting.get('crop', [0, 0, 0, 0])
        if (len(crop) != 4 or any(not isinstance(v, (int, float)) or not 0 <= v < 1 for v in crop)
                or crop[0]+crop[2] >= 1 or crop[1]+crop[3] >= 1):
            raise ValueError(f'Invalid figure crop: {pid}')
        width, _ = raster_pixels(path)
        ppi = width*(1-crop[0]-crop[2])/(width_mm/25.4)
        if ppi+0.01 < minimum:
            raise ValueError(f'{pid}: {ppi:.1f} ppi below {minimum} at {width_mm} mm')
