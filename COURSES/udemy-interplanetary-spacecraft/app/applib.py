"""Shared helpers for appending a scene's content to space-x-study.html (append-only arrays)."""
import json, os, re
D = os.path.dirname(os.path.abspath(__file__))
P = os.path.join(D, 'space-x-study.html')
J = lambda x: json.dumps(x, ensure_ascii=False)

class App:
    def __init__(self):
        self.s = open(P).read()
    def before_close(self, marker, closer, text):
        i = self.s.index(marker); j = self.s.rindex(closer, 0, i)
        self.s = self.s[:j] + text + self.s[j:]
    def rep(self, a, b):
        assert a in self.s, a[:60]
        self.s = self.s.replace(a, b, 1)
    def term_names(self):
        i = self.s.index('const TERMS = ['); j = self.s.index('const ENRICH')
        return set(n.lower() for n in re.findall(r'^ \["((?:[^"\\]|\\.)*)",', self.s[i:j], re.M))
    def add_scene(self, sc):
        self.before_close("// Multiple-choice questions.", "];", " " + ("{id:%s, n:%d, name:%s, color:%s, sec:%s,\n  story:%s,\n  say:%s,\n  draw:%s,\n  why:%s,\n  deep:%s},\n" % (
            J(sc["id"]), sc["n"], J(sc["name"]), J(sc["color"]), J(sc["sec"]), J(sc["story"]), J(sc["say"]), J(sc["draw"]), J(sc["why"]), J(sc["deep"]))))
    def add_mc(self, sid, mc):
        self.before_close("// Explain-why prompts", "];", "".join(" {s:%s, q:%s, o:%s, a:%d, x:%s},\n" % (J(sid), J(q), J(o), a, J(x)) for q, o, a, x in mc))
    def add_why(self, sid, why):
        self.before_close("// Flashcards:", "];", "".join(" {s:%s, q:%s, a:%s},\n" % (J(sid), J(q), J(a)) for q, a in why))
    def add_cards(self, sid, cards):
        self.before_close("const PROGRAMS", "];", "".join(" [%s,%s,%s],\n" % (J(a), J(b), J(sid)) for a, b in cards))
    def add_terms(self, sid, label, terms):
        have = self.term_names(); keep = []; skipped = []
        for t in terms:
            (skipped if t[0].lower() in have else keep).append(t)
        self.before_close("// Concept-level detail for core terms", "];", " // --- %s\n" % label + "".join(" [%s,%s,%s,%s],\n" % (J(a), J(b), J(c), J(sid)) for a, b, c in keep))
        print('terms added', len(keep), 'skipped as duplicates:', [t[0] for t in skipped])
    def add_enrich(self, enrich):
        self.before_close("const NUMBERS", "};", "".join(" %s:{c:%s,e:%s,x:%s,l:%s},\n" % (J(k), J(v[0]), J(v[1]), J(v[2]), J(v[3])) for k, v in enrich.items()))
    def add_mech(self, sid, text):
        self.before_close("const INTERVALS", "};", " %s:%s,\n" % (sid, J(text)))
    def add_formulas(self, sid, rows):
        self.rep(' ],\n constants:[', "".join('  [%s,%s,%s,%s],\n' % (J(a), J(b), J(c), J(sid)) for a, b, c in rows) + ' ],\n constants:[')
    def add_missions(self, rows):
        self.rep('  ["Engine families",', "".join('  [%s,%s],\n' % (J(a), J(b)) for a, b in rows) + '  ["Engine families",')
    def add_program(self, key, prog, before="full"):
        m = re.search(r'const PROGRAM_ORDER=(\[[^\]]*\]);', self.s)
        order = json.loads(m.group(1)); order.insert(order.index(before), key)
        self.s = self.s.replace(m.group(0), 'PROGRAMS.%s=%s;\nconst PROGRAM_ORDER=%s;' % (key, J(prog), json.dumps(order, separators=(',', ':'))), 1)
    def save(self):
        open(P, 'w').write(self.s); print('patched')
