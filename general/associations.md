Ther are various kinds of associations that we see in [UML diagrams](https://www.uml-diagrams.org/).  
Associations are techniques for object composition.

![](https://i.stack.imgur.com/smuC7.jpg)

|Attribute|Composition           |Aggregation      |Dependency                |Inheritance       |Realize/Implementation|
|---------|----------------------|-----------------|--------------------------|------------------|----------------------|
|Lifetime |Owner's Lifetime      |Independent      |Independent               |Derived's Lifetime|Independent           |
|Relation |part-of               |has              |depends-on                |is-a              |     ???              |
|Generally|Object                |Collection       |Service                   |Basic-Attributes  |Instance/Extension    |
|Example  |battery part-of laptop|Library has books|fan depends-on electricity|Car is-a Vehicle  |Baleno is-a Car       |
