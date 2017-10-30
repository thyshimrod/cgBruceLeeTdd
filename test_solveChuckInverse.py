import unittest
from main import SolveChuckInverse


class TestSolveChuckInverse(unittest.TestCase):
    def setUp(self):
        self.instanceSolve = SolveChuckInverse()

    def testCheckFirstElementOne(self):
        self.assertEqual("1", SolveChuckInverse.grabfirstelement("0"))

    def testCheckFirstElementZero(self):
        self.assertEqual("0", SolveChuckInverse.grabfirstelement("00"))

    def testCheckFirstElementInvalid(self):
        self.assertEqual("INVALID", SolveChuckInverse.grabfirstelement("000"))

    def testCheckPairing(self):
        self.assertEqual("INVALID", SolveChuckInverse.solve("00 0 00"))

    def testValidSequence(self):
        self.assertEqual("INVALID", SolveChuckInverse.solve("00 0 1 1"))

    def testUnaryToBinary(self):
        self.assertEqual("1000001", SolveChuckInverse.unarytobinary("0 0 00 00000 0 0"))

    def testLenOfBinary(self):
        self.assertEqual("INVALID", SolveChuckInverse.solve("0 0 00 000000 0 0"))

    def testBinaryToDecimal(self):
        self.assertEqual(65, SolveChuckInverse.binarytonumber("1000001"))

    def testSolveA(self):
        self.assertEqual("A", SolveChuckInverse.solve("0 0 00 00000 0 0"))

    def testSolveA(self):
        self.assertEqual("AA", SolveChuckInverse.solve("0 0 00 00000 0 0 0 0 00 00000 0 0"))

    def testSolveBruce_Lee(self):
        self.assertEqual("Bruce Lee", SolveChuckInverse.solve("0 0 00 0000 0 0 00 0 0 000 00 00 0 0 00 0 0 000 00 0 0 0 00 0 0 000 00 000 0 0000 00 00 0 0 00 0 0 0 00 0 0 0 00 00000 0 0 00 00 0 00 00 00 0 00 00 00 0 0 00 0 0 000 00 00 0 0 00 0 0 0"))


if __name__ == '__main__':
    unittest.main()