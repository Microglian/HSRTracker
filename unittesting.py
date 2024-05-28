import unittest
import main


class GachaTests(unittest.TestCase):
    def setUp(self):
        main.tabset.reload()


    # Use Case 1: A gacha task can be added
    def test_add_gacha_task(self):
        main.gacha_add_task("Low")
        self.assertEqual(main.tabset.gachasource.tasks[-1].objectname, "Acheron")
    
    
    # Use Case 2: A gacha task can be deleted
    def test_del_gacha_task(self):
        main.gacha_add_task("Low")
        main.gacha_delete_task(main.tabset.gachasource.tasks[-1].uuid)
        self.assertNotEqual(main.tabset.gachasource.tasks[-1].objectname, "Acheron")
    
    
    # Use Case 3: A gacha task can have object changed
    def test_set_task_object(self):
        main.gacha_add_task("Low")
        main.gacha_set_object(main.tabset.gachasource.tasks[-1].uuid, "Kafka")
        self.assertEqual(main.tabset.gachasource.tasks[-1].objectname, "Kafka")
    
    # Use Case 4: A gacha task can have target changed
    def test_set_task_target(self):
        main.gacha_add_task("Low")
        main.gacha_set_target(main.tabset.gachasource.tasks[-1].uuid, "E3")
        self.assertEqual(main.tabset.gachasource.tasks[-1].target, "E3")
    
    
    # Use Case 5: A gacha task can have priority changed
    def test_set_task_priority(self):
        main.gacha_add_task("Low")
        main.gacha_change_priority(main.tabset.gachasource.tasks[-1].uuid, "Med")
        self.assertEqual(main.tabset.gachasource.tasks[-1].priority, "Med")
    
if __name__ == "__main__":
    unittest.main()