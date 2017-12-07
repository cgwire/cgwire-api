from tests.base import ApiDBTestCase

from zou.app.models.entity import Entity

from zou.app.utils import fields


class EntityTestCase(ApiDBTestCase):

    def setUp(self):
        super(EntityTestCase, self).setUp()
        self.generate_fixture_project_status()
        self.generate_fixture_project()
        self.generate_fixture_entity_type()
        self.generate_data(
            Entity,
            3,
            entities_out=[],
            entities_in=[],
            project_id=self.project.id,
            entity_type_id=self.entity_type.id
        )

    def test_get_entities(self):
        entities = self.get("data/entities")
        self.assertEquals(len(entities), 3)

    def test_get_entity(self):
        entity = self.get_first("data/entities")
        entity_again = self.get("data/entities/%s" % entity["id"])
        self.assertEquals(entity, entity_again)
        self.get_404("data/entities/%s" % fields.gen_uuid())

    def test_create_entity(self):
        data = {
            "name": "Cosmos Landromat",
            "description": "Video game trailer.",
            "project_id": self.project.id,
            "entity_type_id": self.entity_type.id
        }
        self.entity = self.post("data/entities", data)
        self.assertIsNotNone(self.entity["id"])

        entities = self.get("data/entities")
        self.assertEquals(len(entities), 4)

    def test_update_entity(self):
        entity = self.get_first("data/entities")
        data = {
            "name": "Cosmos Landromat 2"
        }
        self.put("data/entities/%s" % entity["id"], data)
        entity_again = self.get("data/entities/%s" % entity["id"])
        self.assertEquals(data["name"], entity_again["name"])
        self.put_404("data/entities/%s" % fields.gen_uuid(), data)

    def test_delete_entity(self):
        entities = self.get("data/entities")
        self.assertEquals(len(entities), 3)
        entity = entities[0]
        self.delete("data/entities/%s" % entity["id"])
        entities = self.get("data/entities")
        self.assertEquals(len(entities), 2)
        self.delete_404("data/entities/%s" % fields.gen_uuid())
