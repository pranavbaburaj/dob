const ARGUMENTS = ["build"]

export class ArgumentParser {
    private arguments:Array<string>;

    constructor(args:Array<string>) {
        this.arguments = args
    }

    public startEvaluation():any {
        for (var index = 0; index < this.arguments.length; index++){
            // the argument index
            var currentArgument = this.arguments[index]
            if(currentArgument == "build"){
            } else {
                console.error(`Command not found:[${currentArgument}]`)
            }
        }
    }
}