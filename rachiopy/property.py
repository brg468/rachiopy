"""PropertyService calls."""

from rachiopy.rachioobject import RachioObject


class Property(RachioObject):
    """Property service class."""

    def list_properties(self, user_id: str):
        """Retrieve a list of properties by user ID.

        For more info of the content in the response see:
        https://rachio.readme.io/reference/propertyservice_listproperties

        :param user_id: Person's unique id
        :type user_id: str

        :return: The return value is a tuple of (response, content), the first
            being and instance of the httplib2.Response class, the second
            being a string that contains the response entity body (Python
            object if it contains JSON).
        :rtype: tuple
        """

        path = f"property/listProperties/{user_id}"
        return self.valve_get_request(path)

    def get_property(self, property: str):
        """Retrieve the information for a specific property.
        
        For more info of the content in the response see:
        https://rachio.readme.io/reference/propertyservice_getproperty

        :param property: Property's unique id
        :type property: str

        :return: The return value is a tuple of (response, content), the first
            being and instance of the httplib2.Response class, the second
            being a string that contains the response entity body (Python
            object if it contains JSON).
        :rtype: tuple
        """

        path = f"property/getProperty/{property}"
        return self.valve_get_request(path)

    def find_property_by_entity(self, entity_id: str, category: str):
        """Retrieve the property from an entity id.
        
         For more info of the content in the response see:
         https://rachio.readme.io/reference/propertyservice_findpropertybyentity

         :param entity_id: Entity ID
         :type entity: str

         :param category: One of location, base_station, or lighting_area
         :type category: str

         :return: The return value is a tuple of (response, content), the first
            being and instance of the httplib2.Response class, the second
            being a string that contains the response entity body (Python
            object if it contains JSON).
        :rtype: tuple
         """

        supported_categories = ["location", "base_station", "lighting_area"]

        assert category in supported_categories
            #raise ValueError(f"Category not supported. Options are {supported_categories}")

        path = f"property/findPropertyByEntity?resource_id.{category}_id={entity_id}"
        return self.valve_get_request(path)
