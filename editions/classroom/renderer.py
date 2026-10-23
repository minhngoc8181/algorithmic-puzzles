"""Pictorial student book and a plain teaching reference."""
from pathlib import Path
from copy import deepcopy
import os
import re
from tools.figure_models import caption, diagram, instance_table
from tools.artwork import raster_pixels


def bodytex(value):
    """Escape prose separately from authored TeX mathematics."""
    parts = re.split(r'(\$[^$]*\$)', value)
    for i in range(0, len(parts), 2):
        parts[i] = re.sub(r'(?<!\\)([%&#_])', r'\\\1', parts[i])
    value = ''.join(parts)
    value = re.sub(r'\$([^$]*)\$', lambda m: '$'+m[1].replace('),(', r'),\allowbreak(')+'$', value)
    return '\n\\par\n'.join(part.strip().replace('\n', r'\\'+'\n') for part in value.split('\n\n'))


def math_teacher(value):
    substitutions = [
        ('2^m>=1000', r'$2^m\ge 1000$'),
        ('4^5=1024', r'$4^5=1024$'),
        ('=1 - sum_{k=51}^{100}1/k', r'$1-\sum_{k=51}^{100}\frac1k$'),
        ('(3^k-1)/2', r'$(3^k-1)/2$'),
        ('(floor k phi, floor k phi^2)', r'$(\lfloor k\varphi\rfloor,\lfloor k\varphi^2\rfloor)$'),
        ('2^9 tập', r'$2^9$ tập'),
    ]
    parts = re.split(r'(\$[^$]*\$)', value)
    for i in range(0, len(parts), 2):
        for old, new in substitutions:
            parts[i] = parts[i].replace(old, new)
    return bodytex(''.join(parts))


PREAMBLE = r'''\documentclass[11pt,a4paper,twoside]{article}
\usepackage[inner=22mm,outer=21mm,top=24mm,bottom=23mm]{geometry}
\usepackage{fontspec}
\setmainfont{CharisSIL}[Path=../fonts/,Extension=.ttf,UprightFont=*-Regular,BoldFont=*-Bold,ItalicFont=*-Italic,BoldItalicFont=*-BoldItalic]
\setsansfont{Inter}[Path=../fonts/,Extension=.ttf,UprightFont=*-Regular,BoldFont=*-Bold,ItalicFont=*-Italic]
\usepackage{amsmath,amssymb,mathtools,booktabs,enumitem,needspace}
\usepackage{tikz}
\usetikzlibrary{arrows.meta,calc,positioning,shapes.geometric}
\usepackage{xcolor,graphicx,fancyhdr,lastpage,titlesec,hyperref,adjustbox,wrapfig}
\definecolor{ink}{HTML}{18283E}
\definecolor{ocean}{HTML}{28557D}
\definecolor{teal}{HTML}{168C89}
\definecolor{amber}{HTML}{DA9A22}
\definecolor{coral}{HTML}{C76A52}
\definecolor{muted}{HTML}{586D80}
\definecolor{slate}{HTML}{586D80}
\definecolor{softline}{HTML}{D6E0E9}
\definecolor{cloud}{HTML}{F4F7FA}
\definecolor{titlegold}{HTML}{D4931A}
\definecolor{titlegolddeep}{HTML}{7D5112}
\definecolor{titlecyan}{HTML}{1BA7BD}
\definecolor{titlecyandeep}{HTML}{0D566B}
\hypersetup{colorlinks=true,linkcolor=ocean,urlcolor=teal,pdftitle={Câu đố giải thuật}}
\setlength{\parindent}{0pt}
\setlength{\parskip}{4.5pt plus .5pt}
\setlength{\columnsep}{5mm}
\setlength{\intextsep}{2mm}
\setlength{\emergencystretch}{1.5em}
\widowpenalty=10000
\clubpenalty=10000
\raggedbottom
\renewcommand{\contentsname}{Mục lục}
\setlength{\headheight}{14pt}
\pagestyle{fancy}\fancyhf{}
\fancyhead[LE,RO]{\sffamily\footnotesize CÂU ĐỐ GIẢI THUẬT}
\fancyfoot[LE,RO]{\sffamily\footnotesize\textcolor{muted}{\thepage}}
\renewcommand{\headrulewidth}{0.28pt}
\titleformat{\section}{\sffamily\bfseries\Large\color{ink}}{}{0pt}{}
\newcommand{\figfont}{\sffamily\fontsize{10}{12}\selectfont}
\newcommand{\figcaption}[1]{\par\vspace{1mm}{\centering\sffamily\fontsize{9.5}{12}\selectfont\color{muted}#1\par}}
\newcounter{puzzle}
\newcommand{\rating}[1]{%
 \foreach \i in {1,...,5}{%
  \ifnum\i>#1\relax
    \tikz[baseline=-.5ex]{\node[star,star points=5,star point ratio=2,inner sep=0pt,minimum size=2.45mm,fill=white,draw=amber,line width=.33pt] {}; }%
  \else
    \tikz[baseline=-.5ex]{\node[star,star points=5,star point ratio=2,inner sep=0pt,minimum size=2.45mm,fill=amber,draw=amber,line width=.33pt] {}; }%
  \fi
 }%
}
\newcommand{\puzzhead}[2]{\refstepcounter{puzzle}%
 \noindent\begin{minipage}[t]{\dimexpr\linewidth-23mm\relax}\vspace{0pt}
 {\sffamily\bfseries\large\color{ink}\strut\thepuzzle.\ #1\par}
 \end{minipage}\hfill\begin{minipage}[t]{21mm}\vspace{0pt}\raggedleft\strut\rating{#2}\end{minipage}\par\nobreak\vspace{1mm}}
\begin{document}
'''


def cover(count):
    return r'''\begin{titlepage}\thispagestyle{empty}\centering\vspace*{13mm}
\begin{tikzpicture}[x=1cm,y=1cm]
\useasboundingbox (-7.5,-4.4) rectangle (7.5,1.8);
\draw[titlegold!32,line width=1.2pt] (-3.7,.1) arc[start angle=195,end angle=340,x radius=3.8,y radius=.68];
\draw[titlecyan!35,line width=1.2pt] (3.5,.1) arc[start angle=15,end angle=165,x radius=3.6,y radius=.58];
\fill[titlegold] (-3.64,-.02) circle(.07);
\fill[titlecyan] (3.45,.1) circle(.07);
\node[text=titlegolddeep,font=\sffamily\bfseries\fontsize{86}{90}\selectfont,inner sep=0pt] at (.065,-.095) {@COUNT@};
\node[text=titlegold!25!white,font=\sffamily\bfseries\fontsize{86}{90}\selectfont,inner sep=0pt] at (-.025,.035) {@COUNT@};
\node[text=titlegold,font=\sffamily\bfseries\fontsize{86}{90}\selectfont,inner sep=0pt] at (0,0) {@COUNT@};
\node[text=titlegolddeep,font=\sffamily\bfseries\fontsize{38}{44}\selectfont,inner sep=0pt] at (.04,-2.13) {CÂU ĐỐ};
\node[text=titlegold,font=\sffamily\bfseries\fontsize{38}{44}\selectfont,inner sep=0pt] at (0,-2.08) {CÂU ĐỐ};
\node[text=titlecyandeep,font=\sffamily\bfseries\fontsize{38}{44}\selectfont,inner sep=0pt] at (.045,-3.59) {GIẢI THUẬT};
\node[text=titlecyan!15!white,font=\sffamily\bfseries\fontsize{38}{44}\selectfont,inner sep=0pt] at (-.015,-3.515) {GIẢI THUẬT};
\node[text=titlecyan,font=\sffamily\bfseries\fontsize{38}{44}\selectfont,inner sep=0pt] at (0,-3.55) {GIẢI THUẬT};
\end{tikzpicture}
\vspace{13mm}
\adjustbox{max width=\linewidth,center}{\input{../figures/COVER_tikz.tex}}
\vfill
\end{titlepage}
'''.replace('@COUNT@', str(count))


RASTER_CAPTIONS = {
 'NEW-WOLVES':'Hình minh họa tình huống năm con sói và một con cừu.',
 'AP-03':'Hình biểu trưng cho việc thử thuốc; số lọ, số chuột và thời gian theo đề.',
 'NEW-HATS':'Mũ đỏ hoặc xanh; hình chỉ trích một phần đoàn 40 người.',
 'AP-02':'Mỗi lần cân cho ba kết quả: trái nặng, phải nặng hoặc cân bằng.',
 'AP-05':'Hình biểu trưng tòa nhà; ngưỡng vỡ là dữ kiện cần xác định.',
 'AP-28':'Tải, quãng đường và chuối tiêu hao được quy định trong đề.',
 'NEW-COINFLIP':'Bàn cờ có 64 đồng xu; hình minh họa không phải một cách mã hóa.',
 'NEW-BULB':'Một bóng đèn chung; lịch gọi tù nhân do quản ngục quyết định.',
 'NEW-PIRATES':'Năm cướp biển bỏ phiếu theo luật đã cho.',
 'NEW-100BOXES':'100 hộp được đóng lại trước lượt của tù nhân tiếp theo.',
 'NEW-PILLS':'Bốn viên không phân biệt được bằng mắt; được chia chính xác theo đề.',
 'NEW-CHAMELEONS':'Mỗi lần hai con khác màu gặp nhau sẽ đổi sang màu thứ ba.',
 'AP-50':'Ô độc ở góc là dữ kiện của trò chơi.',
 'NEW-SOLDIERS':'Hình chỉ trích một vùng của bàn cờ vô hạn.',
 'NEW-NUTS':'Hình biểu trưng cho 2026 cặp; chỉ thử đai ốc với bu lông.',
}


def illustration(row, settings):
    if settings.get('mode') == 'text-only':
        return ''
    if settings.get('model_kind'):
        row = dict(row, figure_model={'kind': settings['model_kind']})
    caption_override = settings.get('caption')
    model = diagram(row)
    if model:
        content = model
        label = caption(row) if caption_override is None else caption_override
    else:
        figure = row.get('fig')
        if not figure:
            return ''
        if settings.get('raster_path'):
            content = r'\includegraphics[width=\linewidth]{'+settings['raster_path']+'}'
            crop = settings.get('crop', [0, 0, 0, 0])
            if any(crop):
                # Crop only the displayed viewport; retain both source files.
                w, h = settings['native_pixels']
                edges = ' '.join(f'{v*length:.3f}bp' for v, length in zip(crop, (w,h,w,h)))
                # Explicit natural dimensions make the pixel-relative crop
                # independent of a bitmap's optional DPI metadata.
                content = (r'\includegraphics[natwidth='+str(w)+'bp,natheight='+str(h)+
                           r'bp,trim={'+edges+r'},clip,width=\linewidth]{'+settings['raster_path']+'}')
        else:
            content = r'\input{../figures/'+figure+r'_tikz.tex}'
            if figure not in {'AP-01','AP-42','AP-55'}:
                content = r'\adjustbox{max width=\linewidth,center}{'+content+'}'
        label = RASTER_CAPTIONS.get(figure,'') if caption_override is None else caption_override
    result = r'{\centering '+content+r'\par}'+'\n'
    if label:
        result += r'\figcaption{'+bodytex(label)+'}\n'
    return result


def statement(row, settings=None):
    chunks = row['body'].split('{{DATA}}')
    if settings and settings.get('mode')=='data-inline':
        data = r'\par\vspace{2mm}'+'\n'+figure_block(illustration(row,settings),settings)
    else:
        data = instance_table(row.get('instance'))
    return data.join(bodytex(chunk) for chunk in chunks)


def figure_block(image, settings):
    width = str(settings.get('width_mm',105))+'mm'
    return (r'\par{\centering\begin{minipage}{'+width+'}'+image+
            r'\end{minipage}\par}'+'\n'+r'\vspace{2mm}'+'\n')


def beside(text, image, settings):
    """Fixed top alignment for short prose; wrapping for longer plain prose."""
    width = str(settings.get('width_mm', 62))+'mm'
    mode = settings['mode']
    if mode.startswith('wrap-'):
        side = 'r' if mode.endswith('right') else 'l'
        return r'\begin{wrapfigure}{'+side+'}{'+width+'}\n'+image+r'\end{wrapfigure}'+'\n'+text+r'\par'+'\n'
    prose = r'\begin{minipage}[t]{\dimexpr\linewidth-'+width+r'-5mm\relax}\vspace{0pt}'+text+r'\par\end{minipage}'
    art = r'\begin{minipage}[t]{'+width+r'}\vspace{0pt}'+image+r'\end{minipage}'
    return (prose+r'\hfill'+art) if mode.endswith('right') else (art+r'\hfill'+prose)


def entry(row, settings, teacher):
    # The whole card remains readable on one page. A card longer than a page is
    # a build/visual-QA failure rather than a reason to silently shrink fonts.
    start = r'\par\noindent\begin{minipage}{\linewidth}'+'\n'
    start += '\\puzzhead{'+bodytex(row['title'])+'}{'+str(row['difficulty'])+'}\n'
    if teacher:
        content = ''
        for label, field in [('Kết quả.','key'),('Hướng giải.','route'),('Gợi ý tổ chức.','note'),('Ý nghĩa sư phạm.','pedagogy')]:
            if row[field]:
                content += r'\textbf{'+label+'} '+math_teacher(row[field])+r'\par'+'\n'
    else:
        content = statement(row,settings)
    content += r'\par'+'\n'
    image = '' if teacher or settings.get('mode')=='data-inline' else illustration(row, settings)
    mode = settings.get('mode', 'banner-before')
    if image and mode.startswith(('side-', 'wrap-')):
        if '{{DATA}}' in row['body']:
            # A table always regains the whole measure. Do not wrap tabulars.
            before, after = row['body'].split('{{DATA}}', 1)
            content = beside(bodytex(before), image, settings)+r'\par'+'\n'
            content += instance_table(row.get('instance'))+bodytex(after)+r'\par'+'\n'
        else:
            content = beside(content, image, settings)
    elif image:
        banner = figure_block(image,settings)
        content = banner+content if mode=='banner-before' else content+banner
    gap = '6mm' if teacher else '7mm'
    return start+content+'\n'+r'\end{minipage}\par\vspace{'+gap+'}'+'\n'


def document(rows, publication, preamble, teacher):
    out = [preamble]
    breaks = set(publication.get('pagination', {}).get('instructor_breaks_before' if teacher else 'student_breaks_before', []))
    if teacher:
        out += [r'{\sffamily\bfseries\Large\color{ink}'+str(len(rows))+r' câu đố giải thuật · Ghi chú giảng viên\par}',
                r'{\sffamily\fontsize{10}{13}\selectfont\color{muted}Đáp án, hướng giải và ghi chú dạy học.\par}\vspace{3mm}']
    else:
        out.append(cover(len(rows)))
    for i, section in enumerate(publication['sections']):
        if i:
            out.append(r'\clearpage')
        title = section['title']
        out.append(r'\phantomsection\section*{'+title+r'}\addcontentsline{toc}{section}{'+title+r'}\label{sec:'+str(section['id'])+'}\n\\vspace{4mm}\n')
        for row in rows:
            if row['section']==section['id']:
                if row['id'] in breaks:
                    out.append(r'\clearpage')
                out.append(entry(row, publication['layout']['puzzle_layouts'].get(row['id'],{}),teacher))
    return '\n'.join(out)+'\n\\end{document}\n'


def render(rows, publication, output_dir, assets_dir):
    publication = deepcopy(publication)
    for setting in publication['layout']['puzzle_layouts'].values():
        if setting.get('raster_path') and any(setting.get('crop', [])):
            setting['native_pixels'] = raster_pixels(Path(assets_dir)/'figures'/setting['raster_path'])
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    relative = Path(os.path.relpath(assets_dir, output_dir)).as_posix()
    preamble = PREAMBLE.replace('../fonts/',relative+'/fonts/')
    preamble = preamble.replace(r'\begin{document}',r'\graphicspath{{'+relative+'/figures/}}\n'+r'\begin{document}')
    for name in ('student','instructor'):
        current_preamble = preamble
        if name=='student':
            current_preamble = current_preamble.replace(r'\begin{document}',r'\input{../figures/ILL-STYLE.tex}'+'\n'+r'\begin{document}')
        result = document(rows,publication,current_preamble,name=='instructor')
        (output_dir/(name+'.tex')).write_text(result.replace('../figures/',relative+'/figures/'),encoding='utf-8')
