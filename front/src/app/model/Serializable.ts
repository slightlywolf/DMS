/* interface which means that everything that comes from
a json file needs to read from this */
export interface Serializable<T> 
{
    deserialize(input: object): T;
}