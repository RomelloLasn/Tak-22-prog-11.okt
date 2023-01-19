me = {
"eesnimi": "Romello",
"perenimi": "Lasn",
"sünniaasta": "2006",
"elukoht": "Pärsama",
"lemmik magustoit": "jäätis"
}

print(me.get("elukoht"))
print(me["elukoht"])

me.update({"lemmik magustoit": "jäätis" })

for k, v in me.items():
    print(k, v)


if 'isikukood' in me:
    print("isikukood on olemas")
else:
    print("isikukoodi pole")

    print(len(me))

    me.update({"pikkus": len(me)})

    me.pop("sünniaasta")

    del me
