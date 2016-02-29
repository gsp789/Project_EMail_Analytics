from coverage import Coverage
import unittest
import os.path

if __name__ == "__main__":
    cov = Coverage(source='./*', omit=['venv/*', 'civenv/*', 'tests/*'], )

    testmodules = ['tests.unit']

    suite = unittest.TestSuite()

    for t in testmodules:
        try:
            # If the module defines a suite() function, call it to get the suite.
            mod = __import__(t, globals(), locals(), ['suite'])
            suitefn = getattr(mod, 'suite')
            suite.addTest(suitefn())
        except (ImportError, AttributeError):
            # else, just load all the test cases from the module.
            suite.addTest(unittest.defaultTestLoader.loadTestsFromName(t))
    runner = unittest.TextTestRunner()
    cov.start()
    result = runner.run(suite)
    cov.stop()

    if not result.wasSuccessful():
        exit(3)

    percent = round(cov.report(), 4)
    cov.html_report()
    if os.path.isfile('min_cov.txt'):
        file = open('min_cov.txt', 'r')
        min_coverage = float(file.read())
        file.close()
        if percent < min_coverage:
            exit(2)
        else:
            file = open('min_cov.txt', 'w')
            file.write(str(percent))
            file.close()
    else:
        file = open('min_cov.txt', 'w')
        file.write(str(percent))
        file.close()
