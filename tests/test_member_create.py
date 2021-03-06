from bddrest import status, response, when, given

from tests.helpers import LocalApplicationTestCase


class TestMember(LocalApplicationTestCase):

    def test_create(self):
        title = 'alitk777'
        first_name = 'alireza'
        last_name = 'tavakoli'
        gender = 'male'
        email = 'ali@msn.com'
        password = 'Alitk123123'

        with self.given(
                'Create a member',
                '/apiv1/members',
                'CREATE',
                json=dict(
                    title=title,
                    firstName=first_name,
                    lastName=last_name,
                    gender=gender,
                    email=email,
                    password=password,
                ),
        ):
            assert status == 200
            assert response.json['id'] is not None
            assert response.json['title'] == title
            assert response.json['firstName'] == first_name
            assert response.json['lastName'] == last_name
            assert response.json['gender'] == gender
            assert response.json['email'] == email

            when('Trying to pass without form parameters', json={})
            assert status == '400 No Parameter Exists In The Form'

            when('Trying to pass null title', json=given | dict(title=None))
            assert status == '400 title is null'

            when('Trying to pass empty title', json=given - 'title')
            assert status == '400 title field is required'

            when(
                'Trying to pass less than 3 character',
                json=given | dict(title='aq')
            )
            assert status == '400 Title Length Must Be Greater Than 3 ' \
                'Characters and Less than 256 Character'

            when(
                'Trying to pass greater than 256 character',
                json=given | dict(title='a' * 258)
            )
            assert status == '400 Title Length Must Be Greater Than 3 ' \
                'Characters and Less than 256 Character'

            when(
                'Trying to pass null firstname',
                json=given | dict(firstName=None)
            )
            assert status == '400 firstname field is null'

            when(
                'Trying to pass null lastname',
                json=given | dict(lastName=None)
            )
            assert status == '400 lastname field is null'

            when('Trying to pass empty gender', json=given - 'gender')
            assert status == '400 gender field is Required'

            when('Trying to pass null gender', json=given | dict(gender=None))
            assert status == '400 gender field is null'

            when('Trying to pass null title', json=given | dict(email=None))
            assert status == '400 email is null'

            when('Trying to pass empty email', json=given - 'email')
            assert status == '400 Email Not In Form'

            when(
                'Trying to pass invalid email format',
                json=given | dict(email='asd.com')
            )
            assert status == '400 Invalid Email Format'

