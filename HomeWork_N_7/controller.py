from view import what_do as whd, inp_term  as itm
from view import sel_find  as slf, out_res  as our
from model import list_str  as ls, note_find  as nf
from logger import wr_log  as wlog, re_log  as rlog

d = whd()
if not d: wlog(ls(itm()), 'telbook.csv')
elif {d} <= {1, 2}:
    res =  nf(rlog('telbook.csv'), slf(d), d)
    our(res)
else: print(f'Действие не выбрано: {d}')
