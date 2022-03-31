import all
import pytest

@pytest.mark.parametrize("a,b",[(153,True),(370,True),(463,False),(43,True)])
def test_amstr(a,b):
    r = all.amstt(a)
    assert r == b

@pytest.mark.skip
@pytest.mark.parametrize("a,b",[(16,True),(402,True)])
def test_div(a,b):
    r = all.Divideby8(a)
    assert r == b

@pytest.mark.parametrize("a,b,c,d",[(3,1,2,1),(40,30,70,30)])
def test_small(a,b,c,d):
    r = all.smallest(a,b,c)
    assert r == b

@pytest.mark.parametrize("a,b",[(2,"Even"),(3,"Odd")])
def test_eo(a,b):
    r = all.evenorodd(a)
    assert r == b

@pytest.mark.xfail
@pytest.mark.parametrize("a,b",[(121,True),(42222,True)])
def test_pal(a,b):
    #x=121
    r = all.ispalindrome(a)
    assert r == b