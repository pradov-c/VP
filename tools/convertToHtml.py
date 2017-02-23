from json2html import *
import sys
name_file = sys.argv[1]
#inputJson = open(name_file,"r").read()
#html_output = json2html.convert(json = inputJson)
#output = open("resultTest.html","w")
#output.write(html_output)
#output.close()
suite = unittest.TestLoader().loadTestsFromTestCase(TestViews)
unittest.TextTestRunner(verbosity=2)
output = open("resultUnitTest.html","w")
runner = HTMLTestRunner.HTMLTestRunner(stream=output,title='Unit Test Report',
                                          description='Result Unit Test Report')
runner.run(suite)
