import * as fs from "fs";
import * as path from "path"

export namespace Dob {
    export class Database {
        private name:string
        private path_name:string;
        public dict:any;
        private index:number
        private fields:Array<string>
        
        constructor(database_name:string){
            this.name = `${database_name.toString().replace(" ", "_")}.json`
            this.path_name = path.join(process.cwd(), this.name)
            this.dict = {}
            this.index = 1
            this.fields = new Array()
            this.create()
        }
    
        private create():void {
            if (fs.readdirSync(process.cwd()).includes(this.name)) {
                throw new Error("file already exists")
            } else {
                fs.writeFile(this.path_name, "", function(error:NodeJS.ErrnoException)
                {
                    if (error){
                        throw error
                    }
                })
            }
        }
    
        public commit():void {
            fs.writeFile(this.path_name, JSON.stringify(this.dict), function(err) {
                if (err) {
                    throw err;
                } else {
                }
            })
        }
    
        public set_fields(f):void {
            if (Array.isArray(f)) {
                if (this.fields.length == 0) {
                    for (var x = 0; x < f.length; x++){
                        this.fields.push(f[x])
                    }
                } else {
                    throw new Error("Fields are already set")
                }
            } else {
                throw new Error("Field is expected to be an array")
            }
    
        }
    
        public add(f):void {
            if (Array.isArray(f)){
                var dict_value = {
                }
                for (var x = 0; x < f.length; x++){
                    dict_value[this.fields[x].toString()] = f[x]
                }
                this.dict[this.index.toString()] = dict_value
                this.index += 1
                this.commit()
            }else {
                throw new Error("Data is expected to be an array")
            }
        }
    
        public remove_by_id(id):void{
            if (id.toString() in this.dict){
                id = id.toString()
                delete this.dict[id]
                this.commit()
            } 
        }
    }
    
}
