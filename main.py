from crawling.wallet import * 
from crawling.price import *
from tools.plot import * 
from tools.generateProblems import * 
import argparse

class helpCommand(): 
    def generate(): 
        pass

main_parser = argparse.ArgumentParser(description="\x1b[1;36mThis is the helping program !!!\x1b[0m",
        usage="Run 'python %(prog)s --help' for more information",
        formatter_class=argparse.RawTextHelpFormatter, 
        argument_default=argparse.SUPPRESS)
main_parser.add_argument("--generate", nargs=2, type=str, help="\x1b[36mGenerate new problems\x1b[0m", metavar=("<problemSize>", "<resultSize>"))
main_parser.add_argument("--solve", type=str, nargs=1, help="\x1b[36mSolve Problem\x1b[0m", metavar='<ProblemID>')
# main_parser.add_argument("--plot", type=str, nargs=1, help="\x1b[36mPlotting the ProblemData\x1b[0m", metavar="<ProblemID>")
args, noneValid= main_parser.parse_known_args()
inp = vars(args)
if (len(inp) == 0): 
    main_parser.print_help()

if ('generate' in inp.keys()): 
    variable = args.generate
    problemLen = int(variable[0])
    resultLen=int(variable[1])
    stockTickers = ["FPT", "VNI"]
    cryptoTickers = ["btc-usd", "eth-usd"]
    generateProblems().generate(tickers=cryptoTickers, problemLen=problemLen, resultLen=resultLen, typeFinanceProduct='crypto')

if ('solve' in inp.keys()): 
    problemId = int(args.solve[0])
    generateProblems().solve(problemId)

