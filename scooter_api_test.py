
import sender_stand_request




# Elena Khubulava final project autotest 15-Venus
def test_succsess_order_create():
    response = sender_stand_request.create_order()
    track = response.json()["track"]
    assert response.status_code == 201


def test_get_order_by_track():
    response = sender_stand_request.get_order_by_track()
    assert response.status_code == 200


