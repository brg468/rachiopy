"""Property object test module"""

import unittest
from unittest.mock import patch
import uuid

from random import choice
from rachiopy import Property
from tests.constants import VALVE_API_URL, AUTHTOKEN, RESPONSE200, RESPONSE204


class TestPropertyMethods(unittest.TestCase):
    """Class containing the Property test cases."""

    def setUp(self):
        self.property = Property(AUTHTOKEN)

    def test_init(self):
        """Test if the constructor works as expected."""
        self.assertEqual(self.property.authtoken, AUTHTOKEN)

    @patch("requests.Session.request")
    def test_list_properties(self, mock):
        """Test if the list_properties method works as expected."""
        mock.return_value = RESPONSE200

        userid = uuid.uuid4()

        self.property.list_properties(userid)

        args, kwargs = mock.call_args

        # Check that the mock function is called with the rights args.
        self.assertEqual(args[1], f"{VALVE_API_URL}/property/listProperties/{userid}")
        self.assertEqual(args[0], "GET")
        self.assertEqual(kwargs["data"], None)

    @patch("requests.Session.request")
    def test_get_property(self, mock):
        """Test if the get_property method works as expected."""
        mock.return_value = RESPONSE200

        propertyid = uuid.uuid4()

        self.property.get_property(propertyid)

        args, kwargs = mock.call_args

        # Check that the mock function is called with the rights args.
        self.assertEqual(args[1], f"{VALVE_API_URL}/property/getProperty/{propertyid}")
        self.assertEqual(args[0], "GET")
        self.assertEqual(kwargs["data"], None)

    @patch("requests.Session.request")
    def test_get_property_by_entity(self, mock):
        """Test if the get_property_by_entity works as expected."""
        mock.return_value = RESPONSE200

        entityid= uuid.uuid4()
        category = choice(["location", "base_station", "lighting_area"])

        self.property.find_property_by_entity(entityid, category)
        
        args, kwargs = mock.call_args

        # Check that the mock function is called with the rights args.
        self.assertEqual(args[1], f"{VALVE_API_URL}/property/findPropertyByEntity?resource_id.{category}_id={entityid}")
        self.assertEqual(args[0], "GET")
        self.assertEqual(kwargs["data"], None)

    @patch("requests.Session.request")
    def test_get_property_by_entity_exception(self, mock):
        """Test that the get_property_by_entity method catches incorrect categories."""
        mock.return_value = RESPONSE204

        entityid= uuid.uuid4()
        category = choice(["house", "base", "lights"])

        self.assertRaises(AssertionError, self.property.find_property_by_entity, entityid, category)


