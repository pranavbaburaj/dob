const { strict } = require('assert');
const fs = require('fs');
const path = require('path');

class Database {
    constructor(database_name){
        this.name = `${database_name.toString().replace(" ", "_")}.json`
        this.path_name = path.join(process.cwd(), this.name)
        this.dict = {}
        this.index = 1
        this.fields = new Array()
        this.create()
    }

    create() {
        if (fs.readdirSync(process.cwd()).includes(this.name)) {
            throw new Error("file already exists")
        } else {
            fs.writeFile(this.path_name, "", function(err, data) {
                if (err) {
                    throw err;
                } else {

                }
            })
        }
    }

    commit() {
        fs.writeFile(this.path_name, JSON.stringify(this.dict), function(err, data) {
            if (err) {
                throw err;
            } else {
            }
        })
    }

    set_fields(f) {
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

    add(f) {
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

    remove_by_id(id){
        if (id.toString() in this.dict){
            id = id.toString()
            delete this.dict[id]
            this.commit()
        } 
    }
}

module.exports = Database