import unittest
from tools.IoT-Inspector.iot_inspector import IoTInspector

class TestIoTInspector(unittest.TestCase):
    def test_init(self):
        inspector = IoTInspector()
        self.assertEqual(inspector.report_file, "iot_inspector_report.txt")

    def test_log(self):
        inspector = IoTInspector()
        inspector.log("Test message")
        self.assertIn("Test message", inspector.report[0])

    def test_quantum_cryptography(self):
        inspector = IoTInspector()
        inspector.test_quantum_cryptography()
        self.assertIn("Quantum cryptography analysis complete", inspector.report[-1])

if __name__ == "__main__":
    unittest.main()
