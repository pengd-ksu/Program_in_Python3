class Box:
    def __init__(self, name): self.name = name
    def __del__(self): print(f"GC: Box({self.name}) collected")

def demo_1():
    outer = [Box("a"), [Box("b1"), Box("b2")]]  # <- only reference is `outer`
    # When `outer` is deleted, the inner list and all Box objects lose their last refs.
    del outer

demo_1()

def demo_2():
    keep = None
    outer = [Box("c"), [Box("d1"), Box("d2")]]
    keep = outer[1][0]   # keep a separate reference to Box("b1")
    del outer            # outer container and Box("a")/Box("b2") become unreachable
    return keep          # but Box("b1") is still referenced

alive = demo_2()
# GC messages for a and b2, but not for b1
del alive                # now b1 finally becomes collectible
