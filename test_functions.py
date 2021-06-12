"""Here we just test that my functions execute and work"""

from my_module import functions as f

def test_introductions():

    assert f.introductions("HELLO") == True
    assert f.introductions("Goodbye") == False
    assert f.introductions("Hi") == True
    assert f.introductions("Sup") == False
    print("All introductions tests passed")

def test_saying_bye():

    assert f.saying_bye("BYE") == True
    assert f.saying_bye("Hello") == False
    assert f.saying_bye("goodbye") == True
    print("All saying_bye tests passed")
    
def test_get_zodiac():
    
    assert f.get_zodiac(" ") == input("When is your birth month and day? (Month and #)")
    print("All get_zodiac tests passed")
    


                 
    