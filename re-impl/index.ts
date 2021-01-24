import {ArgumentParser} from "./arguments/parser"

var args = process.argv; // the cli arguments passed

// sliced arguments
args = args.slice(2, args.length);

const argumentParserObject = new ArgumentParser(args)
argumentParserObject.startEvaluation()