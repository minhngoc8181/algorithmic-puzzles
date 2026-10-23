"""Check authored instances with exact arithmetic and independent witnesses.

Run directly or through unittest discovery. This is numerical/certificate QA,
not independent peer review of every general theorem in the instructor book.
"""
from collections import Counter, defaultdict, deque
from fractions import Fraction
from functools import lru_cache
import itertools as it
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from tools.common import load_system, edition_rows, solution_for
from tools import numerical as exact


def buffered_trace(records, order):
    by_id = {r['id']:r for r in records}
    w=d=0
    for identifier in order:
        row=by_id[identifier]
        w+=row['wash']
        d=max(d,w)+row['dry']
    return d


def no_wait_trace(records, order):
    by_id={r['id']:r for r in records}
    trace=[]
    washer=dryer=0
    for identifier in order:
        r=by_id[identifier]
        start=max(washer,dryer-r['wash'])
        washer=start+r['wash']
        trace.append([identifier,start,washer,washer,washer+r['dry']])
        dryer=washer+r['dry']
    return dryer,trace


def ant_simulation(records,length):
    """Physical labelled particles with rational event times; no ghost trick."""
    ants=[[r['id'],Fraction(r['position']),1 if r['direction']=='phải' else -1] for r in records]
    events=[]
    now=Fraction(0)
    while ants:
        candidates=[(length-x if v>0 else x) for _,x,v in ants]
        candidates += [(b[1]-a[1])/2 for a,b in zip(ants,ants[1:]) if a[2]>0>b[2]]
        step=min(candidates)
        assert step>0, 'Unexpected simultaneous recollision'
        now+=step
        for a in ants:a[1]+=step*a[2]
        for a,b in zip(ants,ants[1:]):
            if a[1]==b[1] and a[2]>0>b[2]:a[2],b[2]=b[2],a[2]
        remaining=[]
        for identifier,x,v in ants:
            if x in (0,length):events.append((int(now),identifier,'trái' if x==0 else 'phải'))
            else:remaining.append([identifier,x,v])
        ants=remaining
    return events


class Numerical2026(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.system=load_system()
        cls.bank={int(p['id'][3:]):p for p in cls.system['puzzles']}
    def rows(self,n):
        if n==51:
            return solution_for(self.system,self.bank[n])['verification_examples'][0]['instance']['records']
        return self.bank[n]['instance']['records']
    def values(self,n,key):return [r[key] for r in self.rows(n)]
    def answer(self,n):return solution_for(self.system,self.bank[n])['answer']

    def test_2026_comparison_counts_and_odd_boundary(self):
        # A real knockout tree: promote byes without fictitious comparisons.
        def tournament(n):
            leaves=[(i,0) for i in range(n)];count=0
            while len(leaves)>1:
                nxt=[]
                for j in range(0,len(leaves)-1,2):
                    count+=1
                    a,b=leaves[j:j+2]
                    nxt.append((max(a[0],b[0]), max(a[1],b[1])+1))
                if len(leaves)%2:nxt.append(leaves[-1])
                leaves=nxt
            return count,leaves[0][1]
        self.assertEqual((3*2026+1)//2-2,3037)
        self.assertEqual((3*2027+1)//2-2,3039)
        for n in (3,16,32,2026,2027):
            comparisons,depth=tournament(n)
            self.assertEqual(comparisons,n-1)
            self.assertEqual(depth,(n-1).bit_length())
        self.assertEqual(2025+11-1,2035)
        self.assertIn('3037',self.answer(5));self.assertIn('2035',self.answer(6))

    def test_bridge_weights_nim_and_wythoff(self):
        self.assertEqual(exact.bridge(self.values(7,'time')),80)
        weights=[3**i for i in range(8)]
        # Inductively verify every signed sum, including zero, has no gaps.
        sums={0}
        for weight in weights:sums={x+s*weight for x in sums for s in (-1,0,1)}
        self.assertEqual(sums,set(range(-3280,3281)))
        self.assertEqual(2187+81+1-243,2026)
        heaps=self.bank[23]['instance']['heaps']
        xor=0
        for h in heaps:xor^=h
        self.assertEqual(xor,190);self.assertEqual(heaps[0]^xor,1876)
        # Exact integer check of floor(k*phi) without floating rounding.
        import math
        k=1252
        a=(k+math.isqrt(5*k*k))//2
        self.assertEqual((a,a+k),(2025,3277))

    def test_twelve_coin_decision_tree_all_24_hypotheses(self):
        def compare(left,right,coin,sign):
            return sign*((coin in left)-(coin in right))
        def identify(coin,sign):
            first=compare([1,2,3,4],[5,6,7,8],coin,sign)
            if first==0:
                second=compare([9,10,11],[1,2,3],coin,sign)
                if second==0:return 12,compare([12],[1],coin,sign)
                third=compare([9],[10],coin,sign)*second
                return (9 if third>0 else 10 if third<0 else 11),second
            # Orient every unbalanced first result to the left-heavy case.
            second=compare([1,2,5],[3,4,6],coin,sign)*first
            if second>0:
                third=compare([1],[2],coin,sign)*first
                return (1,first) if third>0 else (2,first) if third<0 else (6,-first)
            if second<0:
                third=compare([3],[4],coin,sign)*first
                return (3,first) if third>0 else (4,first) if third<0 else (5,-first)
            third=compare([7],[8],coin,sign)*first
            return (7,-first) if third<0 else (8,-first)
        for coin,sign in it.product(range(1,13),(-1,1)):
            self.assertEqual(identify(coin,sign),(coin,sign))

    def test_fixed_questions_with_one_lie(self):
        words=[]
        for value in range(16):
            bits=[(value>>i)&1 for i in range(4)]
            a,b,c,d=bits
            word=[a^b^d,a^c^d,a,b^c^d,b,c,d]
            words.append(word)
        self.assertEqual(min(sum(x!=y for x,y in zip(a,b)) for a,b in it.combinations(words,2)),3)
        self.assertGreater(16*(1+6),2**6)
        self.assertLessEqual(16*(1+7),2**7)

    def test_information_filtering_and_ages(self):
        self.assertEqual(sum(1 for x in range(2,100) for y in range(x+1,100) if x+y<=100),2352)
        self.assertEqual(exact.sum_product(),[(4,13)])
        triples=[(a,b,c) for a in range(1,37) for b in range(a,37) for c in range(b,37) if a*b*c==36]
        grouped=defaultdict(list)
        for t in triples:grouped[sum(t)].append(t)
        self.assertEqual({s:ts for s,ts in grouped.items() if len(ts)>1},{13:[(1,6,6),(2,2,9)]})
        self.assertEqual([t for t in grouped[13] if t[1]<t[2]],[(2,2,9)])
        days,counts=exact.birthday(self.rows(57))
        self.assertEqual(days,[{'month':6,'day':10}]);self.assertEqual(counts,[20,13,3,1])

    def test_split_compound_states_and_bowling(self):
        # Winning/losing oracle on full multisets, independent of XOR labels.
        @lru_cache(None)
        def win(state):
            for i,n in enumerate(state):
                for a in range(1,(n+1)//2):
                    child=tuple(sorted(state[:i]+state[i+1:]+(a,n-a)))
                    if not win(child):return True
            return False
        for a in range(1,12):
            for b in range(1,8):
                self.assertEqual(win(tuple(sorted((a,b)))),bool(exact.grundy_split(a)[0]^exact.grundy_split(b)[0]))
        self.assertEqual(exact.grundy_split(10)[0],0)
        g,moves=exact.grundy_split(2026)
        self.assertEqual(g,38);self.assertIn(72,moves)
        for n in range(1,80):
            self.assertNotEqual(exact.kayles([n])[0],0) # full line admits mirror strategy
        g,moves=exact.kayles(self.bank[26]['instance']['segments'])
        self.assertEqual(g,7);self.assertIn((1,2,1),moves)

    def test_coins_printer_and_adjacent_merge(self):
        self.assertEqual(exact.coin_game(self.values(27,'value')),372)
        self.assertEqual(exact.adjacent_merge(self.values(40,'size'))[0],1353)
        self.assertEqual(exact.strange_printer(self.bank[41]['instance']['text']),19)
        # Breadth-first printer oracle over literal partially printed strings.
        for length in range(1,5):
            start='_'*length;queue=deque([start]);distance={start:0}
            while queue:
                s=queue.popleft()
                for l in range(length):
                    for r in range(l+1,length+1):
                        for c in 'AB':
                            t=s[:l]+c*(r-l)+s[r:]
                            if t not in distance:distance[t]=distance[s]+1;queue.append(t)
            for s in map(''.join,it.product('AB',repeat=length)):
                self.assertEqual(exact.strange_printer(s),distance[s])
        # Exhaust all actual adjacent merging sequences for a small case.
        def literal_merge(values):
            if len(values)==1:return 0
            return min(values[i]+values[i+1]+literal_merge(values[:i]+(values[i]+values[i+1],)+values[i+2:]) for i in range(len(values)-1))
        for values in ((3,1,4,1),(4,9,2,6,1)):
            self.assertEqual(exact.adjacent_merge(values)[0],literal_merge(values))

    def test_lights_witnesses_and_minimum(self):
        grid=self.bank[31]['instance']['grid'];solutions=exact.lights(grid)
        self.assertEqual(len(solutions),4);self.assertEqual(min(s.bit_count() for s in solutions),6)
        for s in solutions:
            copy=[r[:] for r in grid]
            for i in range(25):
                if s>>i&1:
                    r,c=divmod(i,5)
                    for rr,cc in ((r,c),(r-1,c),(r+1,c),(r,c-1),(r,c+1)):
                        if 0<=rr<5 and 0<=cc<5:copy[rr][cc]^=1
            self.assertFalse(any(map(any,copy)))
        # Row-chasing independently enumerates only the 32 first rows.
        successful=[]
        for mask in range(32):
            board=[r[:] for r in grid];presses=0
            def press(r,c):
                nonlocal presses
                presses+=1
                for rr,cc in ((r,c),(r-1,c),(r+1,c),(r,c-1),(r,c+1)):
                    if 0<=rr<5 and 0<=cc<5:board[rr][cc]^=1
            for c in range(5):
                if mask>>c&1:press(0,c)
            for r in range(1,5):
                for c in range(5):
                    if board[r-1][c]:press(r,c)
            if not any(board[-1]):successful.append(presses)
        self.assertEqual(len(successful),4);self.assertEqual(min(successful),6)

    def test_geometry_rankings_and_gas(self):
        self.assertEqual(exact.closest_pairs(self.rows(37)),(13,[['P07','P24']]))
        self.assertEqual(exact.inversions(self.rows(38)),153)
        self.assertEqual(exact.skyline(self.rows(39)),[[2,11],[5,17],[14,23],[27,19],[36,7],[38,21],[44,13],[50,0],[54,10],[56,16],[63,0]])
        self.assertEqual(exact.gas_starts(self.rows(42)),[3,5,7,9,10,11,13])

    def test_merge_intervals_and_weighted_schedule(self):
        self.assertEqual(exact.rope_cost(self.values(35,'length'))[0],2095)
        @lru_cache(None)
        def unrestricted(values):
            if len(values)==1:return 0
            return min(a+b+unrestricted(tuple(sorted([v for k,v in enumerate(values) if k not in (i,j)]+[a+b])))
                       for i,a in enumerate(values) for j,b in enumerate(values) if i<j)
        for values in ((1,2,3,9),(5,17,2,8,11)):
            self.assertEqual(exact.rope_cost(values)[0],unrestricted(tuple(sorted(values))))
        records=self.rows(43);points,cert=exact.stabbing(records)
        self.assertEqual(points,[6,13,20,28,35,43,51])
        self.assertTrue(all(any(r['left']<=p<=r['right'] for p in points) for r in records))
        by_id={r['id']:r for r in records}
        self.assertTrue(all(by_id[a]['right']<by_id[b]['left'] or by_id[b]['right']<by_id[a]['left'] for a,b in it.combinations(cert,2)))
        # Enumerate all schedules rather than a second weighted-interval DP.
        records=self.rows(44);best=0
        for mask in range(1<<len(records)):
            chosen=sorted([r for i,r in enumerate(records) if mask>>i&1],key=lambda r:r['start'])
            if all(a['end']<=b['start'] for a,b in zip(chosen,chosen[1:])):best=max(best,sum(r['reward'] for r in chosen))
        self.assertEqual(best,220);self.assertEqual(exact.weighted_schedule(records)[0],best)

    def test_partition_packing_matching_and_cover(self):
        difference,team=exact.partition(self.rows(45));by_id={r['id']:r for r in self.rows(45)}
        self.assertEqual(difference,0)
        self.assertEqual(2*sum(by_id[i]['strength'] for i in team),sum(r['strength'] for r in by_id.values()))
        count,groups=exact.bin_packing(self.rows(46),100);by_id={r['id']:r for r in self.rows(46)}
        self.assertEqual(count,9);self.assertEqual(len(groups),count)
        self.assertEqual(sorted(it.chain.from_iterable(groups)),sorted(by_id))
        self.assertTrue(all(sum(by_id[i]['weight'] for i in g)<=100 for g in groups))
        self.assertEqual((sum(r['weight'] for r in by_id.values())+99)//100,9)
        assignments=exact.matching(self.rows(47));by_id={r['id']:r for r in self.rows(47)}
        self.assertEqual(len(assignments),12);self.assertEqual(len(set(assignments.values())),12)
        self.assertTrue(all(p in by_id[i]['accepts'] for i,p in assignments.items()))
        modified=[dict(r) for r in self.rows(47)]
        for r in modified:
            if r['id']=='C':r['accepts']=[5]
            if r['id']=='D':r['accepts']=[2,5,7]
        subset=[r for r in modified if r['id'] in 'ABCD']
        self.assertEqual(set().union(*(set(r['accepts']) for r in subset)),{2,5,7})
        self.assertLess(len(exact.matching(modified)),12)
        cover=exact.set_cover(self.rows(48),self.bank[48]['instance']['universe'])
        self.assertEqual(cover,['A','B','E','H'])

    def test_deadline_and_ski_discrete_boundary(self):
        score,schedule=exact.deadlines(self.rows(50));by_id={r['id']:r for r in self.rows(50)}
        self.assertEqual(score,590)
        self.assertTrue(all(day<=by_id[i]['deadline'] for day,i in schedule.items()))
        # Scheduling feasibility for each subset follows sorted deadlines.
        best=0
        for mask in range(1<<len(by_id)):
            selected=sorted([r for j,r in enumerate(by_id.values()) if mask>>j&1],key=lambda r:r['deadline'])
            if all(k<=r['deadline'] for k,r in enumerate(selected,1)):best=max(best,sum(r['reward'] for r in selected))
        self.assertEqual(best,590)
        # Enumerate every purchase day worth considering and every critical horizon.
        ratios=[]
        for day in range(1,1000):
            horizons={1,day,max(1,day-1),289,290,1000}
            worst=max(Fraction(7*n if n<day else 7*(day-1)+2026,min(7*n,2026)) for n in horizons)
            ratios.append((worst,day))
        self.assertEqual(min(ratios),(Fraction(4042,2023),289))
        self.assertGreater(Fraction(4049,2026),Fraction(4042,2023))

    def test_parallel_cooking_bounds_and_independent_small_oracle(self):
        records=self.rows(53);by_id={r['id']:r for r in records}
        for m,expected in ((2,241),(3,165),(4,130)):
            value,groups=exact.parallel_cooking(records,m)
            self.assertEqual(value,expected)
            self.assertEqual(sorted(it.chain.from_iterable(groups)),sorted(by_id))
            self.assertEqual(max(sum(by_id[i]['duration'] for i in group) for group in groups),value)
            durations=sorted(r['duration'] for r in records)
            lower=max((sum(durations)+m-1)//m,sum(durations[:(len(durations)+m-1)//m]))
            self.assertEqual(lower,value)
        small=[{'id':str(i),'duration':p} for i,p in enumerate((2,7,5,9,3,6))]
        for m in (2,3):
            optimum=min(max(sum(r['duration'] for r,slot in zip(small,assignment) if slot==j) for j in range(m)) for assignment in it.product(range(m),repeat=len(small)))
            self.assertEqual(exact.parallel_cooking(small,m)[0],optimum)

    def test_preemptive_cooking_actual_schedule(self):
        self.assertEqual(self.rows(58),self.rows(53))
        for m in (2,3,4):
            total=sum(self.values(58,'duration'));T=Fraction(total,m)
            clock=Fraction(0);fragments=[]
            for r in self.rows(58):
                rest=Fraction(r['duration'])
                while rest:
                    stove=int(clock//T);start=clock-stove*T
                    take=min(rest,T-start)
                    fragments.append((r['id'],stove,start,start+take))
                    clock+=take;rest-=take
            self.assertEqual(clock,m*T)
            for r in self.rows(58):
                parts=[f for f in fragments if f[0]==r['id']]
                self.assertEqual(sum(f[3]-f[2] for f in parts),r['duration'])
                self.assertTrue(all(a[3]<=b[2] or b[3]<=a[2] for a,b in it.combinations(parts,2)))
            for stove in range(m):
                parts=sorted([f for f in fragments if f[1]==stove],key=lambda f:f[2])
                self.assertTrue(all(a[3]<=b[2] for a,b in zip(parts,parts[1:])))

    def test_two_machine_buffered_and_no_wait(self):
        records=self.rows(54);self.assertEqual(records,self.rows(59))
        johnson,trace=exact.johnson(records);dp,order=exact.flowshop(records)
        self.assertEqual(johnson,214);self.assertEqual(dp,214)
        self.assertEqual(buffered_trace(records,order),214)
        self.assertTrue(any(row[3]>row[2] for row in trace))
        value,order=exact.flowshop(records,no_wait=True)
        self.assertEqual(value,216)
        finish,trace=no_wait_trace(records,order)
        self.assertEqual(finish,value)
        self.assertTrue(all(row[2]==row[3] for row in trace))
        self.assertTrue(all(a[2]<=b[1] and a[4]<=b[3] for a,b in zip(trace,trace[1:])))
        # All permutations on small data check both DPs and the sorting rule.
        for rows in (records[:6],records[6:]):
            names=[r['id'] for r in rows]
            for no_wait in (False,True):
                oracle=min(no_wait_trace(rows,p)[0] if no_wait else buffered_trace(rows,p) for p in it.permutations(names))
                self.assertEqual(exact.flowshop(rows,no_wait=no_wait)[0],oracle)
                if not no_wait:self.assertEqual(exact.johnson(rows)[0],oracle)

    def test_ants_actual_collisions_and_label_recovery(self):
        records=self.rows(51)
        length=solution_for(self.system,self.bank[51])['verification_examples'][0]['instance']['length']
        self.assertEqual(max(min(r['position'],length-r['position']) for r in records),918)
        self.assertEqual(max(max(r['position'],length-r['position']) for r in records),2012)
        labelled=self.rows(60)
        physical=ant_simulation(labelled,length)
        remaining=deque(r['id'] for r in labelled)
        ghost=sorted((r['position'] if r['direction']=='trái' else length-r['position'],r['direction']) for r in labelled)
        recovered=[(t,remaining.popleft() if side=='trái' else remaining.pop(),side) for t,side in ghost]
        self.assertEqual(physical,recovered)
        self.assertEqual([(t,i) for t,i,_ in physical],[(38,'L'),(137,'A'),(263,'K'),(419,'B'),(572,'C'),(749,'J'),(1108,'D'),(1113,'I'),(1285,'H'),(1486,'E'),(1740,'G'),(2012,'F')])
        self.assertEqual(sum(Fraction(1,10000*2**n) for n in range(10)),Fraction(1023,5120000))
        # Every dyadic harmonic block contributes at least 1/2.
        for k in range(8):self.assertGreaterEqual(sum(Fraction(1,n) for n in range(2**k+1,2**(k+1)+1)),Fraction(1,2))

    def test_general_ants_and_classic_six_frogs(self):
        # Enumerate every initial direction on an independently chosen rope.
        length=17;positions=(1,4,9,14);fall_times=[]
        for directions in it.product(('trái','phải'),repeat=len(positions)):
            records=[{'id':str(i),'position':x,'direction':d} for i,(x,d) in enumerate(zip(positions,directions))]
            fall_times.append(max(t for t,_,_ in ant_simulation(records,length)))
        self.assertEqual(min(fall_times),max(min(x,length-x) for x in positions))
        self.assertEqual(max(fall_times),max(max(x,length-x) for x in positions))
        self.assertEqual(self.bank[51]['instance']['kind'],'ants-general')
        self.assertNotIn('{{DATA}}',self.bank[51]['statement'])
        self.assertEqual(self.bank[33]['instance']['n'],3)
        # Breadth-first search proves minimal moves and supplies a legal path.
        for n in range(1,5):
            start='F'*n+'_'+'T'*n;target='T'*n+'_'+'F'*n
            queue=deque([start]);dist={start:0}
            while queue:
                state=queue.popleft()
                if state==target:break
                hole=state.index('_')
                for direction,symbol in ((1,'F'),(-1,'T')):
                    for step in (1,2):
                        old=hole-direction*step
                        if 0<=old<len(state) and state[old]==symbol and (step==1 or state[old+direction]!='_'):
                            chars=list(state);chars[hole],chars[old]=chars[old],chars[hole];child=''.join(chars)
                            if child not in dist:dist[child]=dist[state]+1;queue.append(child)
            self.assertEqual(dist[target],n*n+2*n)
        self.assertIn('15 lượt',self.answer(33))

    def test_selection_and_student_teacher_separation(self):
        rows=edition_rows(self.system)
        self.assertEqual(len(rows),60)
        self.assertEqual([sum(r['section']==s for r in rows) for s in (1,2,3)],[24,18,18])
        groups={r['id']:r['section'] for r in rows}
        for pid in ('PZ-0021','PZ-0020','PZ-0036','PZ-0049'):
            self.assertEqual(groups[pid],1)
        for pid in ('PZ-0001','PZ-0002','PZ-0034','PZ-0027','PZ-0031'):
            self.assertEqual(groups[pid],2)
        order=[r['id'] for r in rows]
        self.assertEqual(order.index('PZ-0058'),order.index('PZ-0053')+1)
        self.assertEqual(order.index('PZ-0059'),order.index('PZ-0054')+1)
        for section in (1,2,3):
            stars=[r['difficulty'] for r in rows if r['section']==section]
            self.assertEqual(stars,sorted(stars))
        self.assertLess([r['id'] for r in rows].index('PZ-0056'),[r['id'] for r in rows].index('PZ-0023'))
        tex=ROOT/'build'/self.system['edition']['id']/'tex'
        if tex.exists():
            student=(tex/'student.tex').read_text(encoding='utf-8')
            instructor=(tex/'instructor.tex').read_text(encoding='utf-8')
            self.assertEqual(student.count(r'\puzzhead{'),60)
            self.assertEqual(instructor.count(r'\puzzhead{'),60)
            for forbidden in ('{{DATA}}','Kết quả.','Hướng thảo luận.','PZ-','Grund','Johnson','McNaughton','Hamming','GF(2)'):
                self.assertNotIn(forbidden,student)
            self.assertNotIn('PZ-',instructor)
            self.assertNotIn('bài bổ sung',instructor)
            self.assertNotIn('Ấn bản',instructor)
            self.assertNotIn('Bản sinh viên',student)
            self.assertNotIn('Ấn bản',student)
            self.assertNotIn(r'\begin{titlepage}',instructor)
            self.assertNotIn(r'\tableofcontents',instructor)
            self.assertNotIn(r'\input{',instructor)
            self.assertEqual(instructor.count('Ý nghĩa sư phạm.'),60)


if __name__=='__main__':unittest.main(verbosity=2)
