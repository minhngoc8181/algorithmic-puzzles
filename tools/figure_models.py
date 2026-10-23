"""Data-derived TeX diagrams: fixed physical fonts, no solution annotations."""
import math
import re


def text(value):
    value = ', '.join(map(str,value)) if isinstance(value,list) else str(value)
    return re.sub(r'(?<!\\)([%&#_])', r'\\\1', value)


def instance_table(instance):
    if not instance:
        return ''
    if instance['kind'] == 'strange-printer':
        return r'\begin{center}\sffamily\fontsize{12}{15}\selectfont '+instance['text']+r'\end{center}'
    columns, records = instance.get('columns'), instance.get('records')
    if not columns:
        return ''
    groups = 2 if len(columns) >= 4 or any(isinstance(r[c['field']],list) for r in records for c in columns) else 3
    if sum(len(c['label']) for c in columns) > 20:
        groups = 2
    if len(records) < 9:
        groups = 2
    count = math.ceil(len(records)/groups)
    specification = r'@{}' + r'@{\hspace{7mm}}'.join('l'*len(columns) for _ in range(groups)) + r'@{}'
    headers = [r'\textbf{'+text(c['label'])+'}' for c in columns] * groups
    result = [r'\par\begingroup\fontsize{10}{12}\selectfont\renewcommand{\arraystretch}{1.18}',
              r'\begin{center}\begin{tabular}{'+specification+'}', r'\toprule', ' & '.join(headers)+r'\\', r'\midrule']
    for i in range(count):
        cells = []
        for group in range(groups):
            j = i+group*count
            cells += [text(records[j][c['field']]) if j<len(records) else '' for c in columns]
        result.append(' & '.join(cells)+r'\\')
    result += [r'\bottomrule\end{tabular}\end{center}\endgroup\par']
    return '\n'.join(result)


CAPTIONS = {
 'comparison':'Chỉ biết quan hệ nặng–nhẹ qua phép cân hai kiện; dấu lược biểu diễn các kiện còn lại.',
 'houses':'S biết tổng, P biết tích; các lời thông báo được nghe công khai.',
 'muddy':'Bảy em nhìn thấy nhau; mỗi vòng trả lời đồng thời.',
 'locks':'Mười một người, mọi nhóm sáu được mở hòm; chưa cho cách chia chìa.',
 'weights':'Tám khối lượng cần chọn; quả cân được dùng ở hai phía hoặc để ngoài.',
 'heaps':'Kích thước đống ghi bằng số; hình biểu trưng, không vẽ từng viên.',
 'split':'Một lượt tách sinh hai đống không bằng nhau; các đống mới cùng tồn tại.',
 'segments':'Năm đoạn đứng tách rời; các quân còn lại không dồn vào khoảng trống.',
 'sequence':'Giữ đúng thứ tự từ trái sang phải; kích thước vật được ghi trên từng ô.',
 'lights':'Vàng: bật; trắng: tắt. Hàng và cột đánh số 1–5.',
 'frogs':'Chín F hướng phải, chín T hướng trái; ô giữa trống.',
 'tromino':'Bảng 64×64 thiếu một ô bất kỳ; ô thiếu trong hình được phóng đại.',
 'coin-row':'Giá trị các đồng tiền theo thứ tự từ trái sang phải.',
 'ropes':'Độ dài của 18 sợi nằm trong bảng; được chọn hai sợi bất kỳ để nối.',
 'points':'Hình dùng cùng tỉ lệ trên hai trục; quyết định chính xác dựa vào tọa độ trong bảng.',
 'rankings':'Hình chỉ trích phần đầu hai bảng; danh sách đủ 24 người ở bảng dữ kiện.',
 'buildings':'Các hình chữ nhật là dữ kiện tòa nhà, không tô sẵn đường bao cần tìm.',
 'printer':'Máy in được ghi đè một đoạn liên tiếp; hình chưa biểu diễn kế hoạch tối ưu.',
 'gas':'Đi một chiều từ trạm 1 đến 16 rồi trở lại; số liệu ở bảng.',
 'intervals':'Hai phần hình dùng cùng thang hoành độ; dấu chấm là đầu mút được tính thuộc đoạn.',
 'activities':'Các thanh là thời gian cố định của tiết mục; chưa đánh dấu lịch được chọn.',
 'teams':'Mỗi người vào đúng một đội; không bắt buộc hai đội cân số người.',
 'elevator':'Sức tải 100 mỗi chuyến; mỗi kiện phải giữ nguyên vẹn.',
 'matching':'Mỗi đường nối là một lựa chọn được chấp nhận, không phải một phân công đã chọn.',
 'committees':'Mỗi đường nối cho biết ứng viên có thể đại diện ủy ban; chưa chọn một tập phủ.',
 'deadlines':'Các ô ngày là chỗ có thể lập lịch; chưa xếp công việc hoặc chọn tiền thưởng.',
 'ants':'Vị trí ban đầu theo bảng; sơ đồ không vẽ các quỹ đạo va chạm.',
 'rubber':'Kiến bò so với mặt dây, đầu phải dịch ra khi dây giãn đều.',
 'stoves':'Bếp hoạt động song song; điều kiện được ngắt món phụ thuộc đúng phiên bản đề.',
 'laundry':'Một công đoạn giặt rồi một công đoạn sấy; quyền chờ được ghi theo phiên bản.',
 'ages':'Ba tuổi chưa biết; số nhà người bạn nhìn thấy chưa cho người đọc.',
 'single-heap':'Một đống chỉ giảm đi, không tách thành nhiều đống.',
 'calendar':'Các ngày ứng viên là dữ kiện chung; không đánh dấu ngày đúng.',
 'questions':'Các câu hỏi phải được ghi trước; không có nhánh hỏi thích nghi theo câu trả lời.',
 'bridge':'Tám người cùng một đèn; các thời gian ở bảng, cầu chỉ chịu tối đa hai người.',
 'ski':'Thuê theo từng ngày hoặc mua một lần; tổng số ngày sử dụng chưa biết.',
}


def caption(row):
    model = row.get('figure_model')
    return CAPTIONS.get(model['kind'],'') if model else ''


def diagram(row):
    model, instance = row.get('figure_model'), row.get('instance') or {}
    if not model:
        return None
    kind = model['kind']
    records = instance.get('records', [])
    out = [r'\begin{tikzpicture}[x=1cm,y=1cm,font=\figfont,line width=.65pt]']
    def node(x,y,label,options=''):
        out.append(f'\\node[{options}] at ({x:.4f},{y:.4f}) {{{text(label)}}};')
    def box(x,y,label,width=1.5,height=.65):
        out.append(f'\\draw[draw=ocean,fill=cloud,rounded corners=2pt] ({x-width/2:.4f},{y-height/2:.4f}) rectangle ({x+width/2:.4f},{y+height/2:.4f});')
        node(x,y,label)
    def arrow(x,y,a,b,label=None):
        out.append(f'\\draw[ocean,-{{Latex[length=2mm]}}] ({x},{y})--({a},{b});')
        if label:node((x+a)/2,(y+b)/2+.25,label)
    if kind == 'comparison':
        for i,label in enumerate(('K1','K2','K3','…','K2026')):box(i*1.7,0,label)
        node(3.4,-1,'Cân hai kiện → một quan hệ nặng–nhẹ')
    elif kind in ('houses','ages'):
        labels=('Nhà x','Nhà y') if kind=='houses' else ('Tuổi a','Tuổi b','Tuổi c')
        for i,label in enumerate(labels):
            x=i*2.3
            box(x,0,label,1.8)
            out.append(f'\\draw[ocean] ({x-.9},.35)--({x},1.1)--({x+.9},.35);')
        node((len(labels)-1)*1.15,-1,'Tổng chưa biết' if kind=='ages' else 'Tổng riêng / tích riêng')
    elif kind == 'muddy':
        for i in range(7):
            x=i*.9
            out.append(f'\\draw[fill=cloud,draw=ocean] ({x},0) circle(.27);\\fill[coral] ({x},.12) circle(.065);')
            node(x,-.55,str(i+1))
    elif kind == 'locks':
        for i in range(11):
            out.append(f'\\draw[fill=cloud,draw=ocean] ({i*.72},0) circle(.2);')
            node(i*.72,-.45,str(i+1))
        box(3.6,-1.45,'Hòm chung',2.5,.75)
    elif kind == 'weights':
        for i in range(8):
            x=i*1.0
            out.append(f'\\draw[fill=teal!12,draw=ocean] ({x-.36},0) rectangle ({x+.36},.6);\\draw[ocean] ({x-.15},.6)--({x-.15},.78)--({x+.15},.78)--({x+.15},.6);')
            node(x,.3,str(i+1))
        node(3.5,-.6,'Khối lượng của tám quả chưa được chọn')
    elif kind in ('heaps','split','single-heap'):
        heaps=instance.get('heaps', [instance.get('n',2026)])
        for i,size in enumerate(heaps):
            x=i*2.0
            for j in range(3):
                out.append(f'\\draw[fill=teal!10,draw=ocean] ({x-j*.1-.25},{j*.18}) rectangle ({x+j*.1+.25},{j*.18+.15});')
            node(x,-.5,str(size))
        if kind=='split':
            arrow(.65,.15,2,.15)
            box(3,.15,'a',1.2);box(5,.15,'b',1.2)
            node(4,-.6,'a + b = 2026; a < b')
        if kind=='single-heap':node(2,0,'Lấy 1, 3 hoặc 4 viên')
    elif kind == 'segments':
        for i,n in enumerate(instance['segments']):
            y=-i*.5
            node(-.6,y,str(i+1))
            for j in range(n):out.append(f'\\draw[draw=ocean,fill=teal!12] ({j*.37:.3f},{y-.11:.3f}) rectangle ({j*.37+.19:.3f},{y+.11:.3f});')
            node(n*.37+.5,y,str(n))
    elif kind in ('sequence','ropes'):
        if kind=='ropes':
            for i in range(5):
                x=i*1.5
                out.append(f'\\draw[teal,line width=2pt] ({x},0)..controls({x+.7},.65)and({x+.8},-.4)..({x+1.1},.1);')
            node(7.7,0,'… 18 sợi')
        else:
            field='size' if instance['kind']=='adjacent-merge' else 'value'
            for i,r in enumerate(records):box(i*.78,0,str(r[field]),.67,.57)
    elif kind == 'lights':
        n=len(instance['grid'])
        for r in range(n):
            node(-.5,-r*.9,str(r+1))
            for c in range(n):
                fill='amber!70' if instance['grid'][r][c] else 'white'
                x,y=c*.9,-r*.9
                out.append(f'\\draw[fill={fill},draw=ocean!60,rounded corners=3pt] ({x-.37:.3f},{y-.37:.3f}) rectangle ({x+.37:.3f},{y+.37:.3f});')
                bulb='amber!85' if instance['grid'][r][c] else 'muted!15'
                out.append(f'\\shade[ball color={bulb},draw=muted!60] ({x:.3f},{y+.08:.3f}) circle(.19);')
                out.append(f'\\fill[muted!75] ({x-.085:.3f},{y-.15:.3f}) rectangle ({x+.085:.3f},{y-.08:.3f});')
                out.append(f'\\draw[muted!60,line width=.5pt] ({x-.055:.3f},{y+.11:.3f})--({x:.3f},{y-.065:.3f})--({x+.055:.3f},{y+.11:.3f});')
        for c in range(n):node(c*.9,.55,str(c+1))
    elif kind=='frogs':
        n=instance['n']
        for i in range(2*n+1):
            box(i*.6,0,'F' if i<n else 'T' if i>n else '',.52,.52)
        arrow(1,-.65,3,-.65);arrow((2*n-1)*.6,-.65,(2*n-4)*.6,-.65)
    elif kind=='tromino':
        size=instance['size'];side=5.12;cell=side/size
        out.append(r'\fill[muted!12] (.08,-.12) rectangle (5.20,5.00);')
        out.append(r'\draw[fill=amber!16,draw=amber!65!black,line width=.8pt] (0,0) rectangle (5.12,5.12);')
        for i in range(size+1):
            p=i*cell
            out.append(f'\\draw[amber!55!black,line width=.16pt] ({p:.5f},0)--({p:.5f},{side}) (0,{p:.5f})--({side},{p:.5f});')
        # An arbitrary illustrative hole, without any partition or tiling.
        hx,hy=int(size*.703125)*cell,int(size*.28125)*cell
        out.append(f'\\fill[white] ({hx:.5f},{hy:.5f}) rectangle ({hx+cell:.5f},{hy+cell:.5f});')
        out.append(f'\\draw[coral,line width=.65pt] ({hx:.5f},{hy:.5f}) rectangle ({hx+cell:.5f},{hy+cell:.5f});')
        out.append(f'\\draw[muted,line width=.5pt] ({hx+cell:.5f},{hy+cell:.5f})--(5.65,3.80);')
        out.append(r'\draw[fill=white,draw=coral,line width=.7pt] (5.65,3.50) rectangle (6.55,4.40);')
        node(6.10,4.80,'Ô đã bỏ')
        node(side/2,-.44,f'{size} × {size}')
        # Three top faces occupy a 2x2 square with the upper-right corner empty.
        for x,y in ((5.75,.75),(6.30,.75),(5.75,1.30)):
            out.append(f'\\fill[amber!60!black] ({x},{y})--({x+.55},{y})--({x+.63},{y-.10})--({x+.08},{y-.10})--cycle;')
            out.append(f'\\draw[fill=amber!22,draw=amber!65!black,line width=.75pt] ({x},{y}) rectangle ({x+.55},{y+.55});')
        node(6.30,2.20,'Miếng chữ L')
    elif kind=='coin-row':
        for i,r in enumerate(records):
            x=i*.83
            out.append(f'\\fill[muted!14] ({x+.025:.4f},-.055) circle(.36);')
            out.append(f'\\draw[fill=amber!45,draw=amber!65!black,line width=.8pt] ({x:.4f},0) circle(.36);')
            out.append(f'\\draw[fill=amber!16,draw=amber!60!black,line width=.45pt] ({x:.4f},0) circle(.31);')
            out.append(f'\\draw[white,line width=.6pt] ({x+.325:.4f},0) arc[start angle=0,end angle=145,radius=.325cm];')
            node(x,0,r['value'],'text=ink')
    elif kind=='points':
        scale=min(13/max(r['x'] for r in records),5.2/max(r['y'] for r in records))
        mx,my=max(r['x'] for r in records)*scale,max(r['y'] for r in records)*scale
        arrow(0,0,mx+.5,0);arrow(0,0,0,my+.5)
        node(mx+.6,0,'x');node(0,my+.7,'y')
        for r in records:out.append(f"\\fill[ocean] ({r['x']*scale:.4f},{r['y']*scale:.4f}) circle(.035);")
        for x in range(0,1001,200):
            if x*scale<=mx:node(x*scale,-.4,str(x))
    elif kind=='rankings':
        for j,key in enumerate(('first','second')):
            node(-1.15,-j,'HĐ '+str(j+1))
            for i,r in enumerate(records[:6]):box(i*1.15,-j,r[key],1.0,.55)
            node(7.0,-j,'…')
    elif kind=='buildings':
        sx, sy = .205, .15
        right = max(r['right'] for r in records)
        top = 5*math.ceil(max(r['height'] for r in records)/5)
        for h in range(5,top+1,5):
            out.append(f'\\draw[softline,line width=.35pt] (0,{h*sy:.3f})--({right*sx:.3f},{h*sy:.3f});')
            node(-.45,h*sy,str(h))
        # Fill first, then draw every outline: overlapping buildings never
        # erase the edges of lower or earlier rectangles.
        for r in records:
            out.append(f"\\fill[teal,fill opacity=.10] ({r['left']*sx:.3f},0) rectangle ({r['right']*sx:.3f},{r['height']*sy:.3f});")
        for r in records:
            out.append(f"\\draw[draw=ocean,line width=.65pt] ({r['left']*sx:.3f},0) rectangle ({r['right']*sx:.3f},{r['height']*sy:.3f});")
        arrow(0,0,right*sx+.4,0)
        arrow(0,0,0,top*sy+.4)
        for x in range(0,right+1,10):
            out.append(f'\\draw[ocean] ({x*sx:.3f},0)--({x*sx:.3f},-.10);')
            node(x*sx,-.38,str(x))
        node(right*sx+.6,0,'x')
        node(0,top*sy+.6,'H')
    elif kind=='printer':
        box(1,1,'Máy in',2.3)
        for i,label in enumerate(instance['text'][:12]):box(i*.55,0,label,.5,.5)
        node(7,0,'…')
    elif kind=='gas':
        n=len(records)
        for i,r in enumerate(records):
            angle=2*math.pi*i/n
            x,y=2.6*math.cos(angle),2.6*math.sin(angle)
            out.append(f'\\draw[fill=cloud,draw=ocean] ({x:.4f},{y:.4f}) circle(.21);')
            node(x,y,r['id'])
        out.append(r'\draw[ocean,-{Latex[length=2mm]}] (3.1,0) arc[start angle=0,end angle=55,radius=3.1];')
    elif kind in ('intervals','activities'):
        half=math.ceil(len(records)/2)
        maximum=max(r['right' if kind=='intervals' else 'end'] for r in records)
        scale=5.8/maximum
        for i,r in enumerate(records):
            panel,index=divmod(i,half);x0=panel*7.1;y=-index*.48
            left,right=(r['left'],r['right']) if kind=='intervals' else (r['start'],r['end'])
            node(x0-.4,y,r['id'])
            out.append(f'\\draw[teal,line width=1.8pt] ({x0+left*scale:.3f},{y:.3f})--({x0+right*scale:.3f},{y:.3f});')
            if kind=='intervals':
                for endpoint in (left,right):out.append(f'\\fill[ocean] ({x0+endpoint*scale:.3f},{y:.3f}) circle(.035);')
        for panel in range(2):
            for tick in range(0,maximum+1,10):node(panel*7.1+tick*scale,-half*.48-.15,str(tick))
    elif kind in ('matching','committees'):
        if kind=='matching':
            left=[r['id'] for r in records];right=list(range(1,instance['positions']+1));edges=[(r['id'],v) for r in records for v in r['accepts']]
            left_title,right_title='Sinh viên','Vị trí'
        else:
            left=instance['universe'];right=[r['id'] for r in records];edges=[(v,r['id']) for r in records for v in r['covers']]
            left_title,right_title='Ủy ban','Ứng viên'
        height=.46*max(len(left),len(right))
        ys={v:height-i*.46 for i,v in enumerate(left)};zs={v:height-i*.46 for i,v in enumerate(right)}
        for a,b in edges:out.append(f'\\draw[softline] (0,{ys[a]:.3f})--(5.8,{zs[b]:.3f});')
        for x,mapping in ((0,ys),(5.8,zs)):
            for label,y in mapping.items():
                out.append(f'\\draw[fill=white,draw=ocean] ({x},{y:.3f}) circle(.22);');node(x,y,label)
        node(0,height+.65,left_title);node(5.8,height+.65,right_title)
    elif kind in ('teams','elevator','deadlines','stoves'):
        if kind=='teams':
            box(1,0,'Đội 1',2.0,.85);box(5,0,'Đội 2',2.0,.85);node(3,1,'20 người → hai nhóm')
        elif kind=='elevator':
            box(2,0,'Tải tối đa 100',3.4,1.15);node(2,-1.0,'18 kiện nguyên vẹn')
        elif kind=='deadlines':
            for i in range(9):box(i*.8,0,str(i+1),.7,.7)
            node(3.2,-.7,'Ngày hoàn thành')
        else:
            for i in range(4):
                x=i*1.85
                box(x,0,'Bếp '+str(i+1),1.65,.8)
                out.append(f'\\draw[ocean] ({x-.4},.75) rectangle ({x+.4},1.05);')
            node(2.775,-.85,'13 món · thời lượng theo bảng')
    elif kind=='laundry':
        box(0,0,'Máy giặt',2.4,.85);box(6.4,0,'Máy sấy',2.4,.85)
        if instance['kind']=='flowshop':box(3.2,0,'Giỏ chờ',2,.7)
        else:node(3.2,.6,'Chuyển ngay')
        arrow(1.3,0,2.1,0);arrow(4.3,0,5.1,0)
    elif kind=='ants':
        length=instance['length'];scale=13.5/length
        out.append(r'\draw[ocean,line width=1.1pt] (0,0)--(13.5,0);')
        for r in records:
            x=r['position']*scale
            out.append(f'\\fill[ink] ({x:.4f},0) circle(.055);')
            node(x,.45,r['id'])
        node(0,-.45,'0');node(13.5,-.45,str(length)+' cm')
    elif kind=='rubber':
        out.append(r'\draw[teal,line width=1.4pt] (0,0)--(7,0);\fill[ink] (.2,0) circle(.075);')
        node(.4,.65,'Kiến');arrow(.5,.2,1.6,.2,'1 cm/giây')
        arrow(7.2,0,9.8,0,'Giãn thêm 100 m')
        node(3.5,-.6,'Dây ban đầu 100 m')
    elif kind=='calendar':
        months=sorted({r['month'] for r in records})
        for i,month in enumerate(months):
            y=-i*.58
            node(0,y,'Tháng '+str(month))
            for j,r in enumerate(r for r in records if r['month']==month):box(2+j*.8,y,str(r['day']),.68,.46)
    elif kind=='questions':
        for i,label in enumerate(('Câu 1','Câu 2','Câu 3','…','Câu m')):box(i*1.65,0,label,1.45,.8)
        node(3.3,-.8,'Ghi trước toàn bộ câu hỏi')
    elif kind=='bridge':
        out.append(r'\draw[ocean,line width=1.3pt] (0,0)--(8,0);\draw[ocean] (0,-.3)--(8,-.3);')
        for i in range(8):
            out.append(f'\\draw[fill=cloud,draw=ocean] ({i*.7},.8) circle(.2);')
        node(3.5,-.8,'Cầu · tối đa hai người một lượt')
    elif kind=='ski':
        box(0,0,'Thuê: 7 / ngày',3.1,.85)
        box(5,0,'Mua: 2026',3.1,.85)
        node(2.5,-.9,'Chưa biết số ngày sẽ dùng')
    else:
        raise ValueError(f'Unknown figure model: {kind}')
    out.append(r'\end{tikzpicture}')
    return '\n'.join(out)
