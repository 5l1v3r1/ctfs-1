s = [
  "moc.udiaB",
  "YWg",
  "moc.eviL",
  "moc.tfosorciM",
  "moc.llamT",
  "ni.oc.elgooG",
  "charCodeAt",
  "moc.oaboaT",
  "moc.smacagnoB",
  "HFK",
  "IFv",
  "push",
  "HMI",
  "moc.yabE",
  "moc.margatsnI",
  "reverse",
  "%% ",
  "N% ",
  "moc.enozekO",
  "moc.koobecaF",
  "moc.dJ",
  "floor",
  "87b",
  "moc.yfipohsyM",
  "MQ ",
  "moc.swennubirT",
  "$!!",
  "%MR",
  "moc.kV",
  "su.mooZ",
  "wLM",
  "nc.063",
  "moc.llamt.nigoL",
  "/gQ",
  "pj.oc.nozamA",
  "nc.aynaiT",
  "4fb",
  "moc.nozamA",
  "moc.enilnotfosorciM",
  "ac4",
  "JHM",
  "gro.aidepikiW",
  "moc.ebutuoY",
  "moc.wolfrevokcatS",
  "moc.rettiwT",
  "moc.revaN",
  "kh.moc.elgooG",
  "29b",
  "1cf",
  "moc.sserpxeilA",
  "0b3",
  "popUpWindow",
  "4e1",
  "nc.moc.aniS",
  "random",
  "moc.llamt.segaP",
  "split",
  "moc.uhoS",
  "join",
  "moc.obieW",
  "moc.tenauhniX",
  "moc.topsgolB",
  "moc.qQ",
  "log",
  "fromCharCode",
  "vt.adnaP",
  "pj.oc.oohaY",
  "height=137,width=137,left=137,top=137",
  "vt.hctiwT",
  ".{1,",
  "length",
  " %$",
  "match",
  "vt.iqnahZ"
]

data = open('script.js').read()

for i, k in enumerate(s):
    a = "_0('{}')".format(hex(i))
    data = data.replace(a, '\"{}\"'.format(k))

with open('script.deob.js', 'w') as f:
    f.write(data)
    