Ther are various kinds of associations that we see in [UML diagrams](https://www.uml-diagrams.org/).  
Associations are techniques for object composition.

![](https://i.stack.imgur.com/smuC7.jpg)

|Attribute|Composition           |Aggregation      |Dependency                |Inheritance       |Realize/Implementation|
|---------|----------------------|-----------------|--------------------------|------------------|----------------------|
|Lifetime |owner's lifetime      |independent      |independent               |derived's lifetime|independent           |
|Relation |part-of               |has              |depends-on                |is-a              |     ???              |
|Generally|object                |collection       |service                   |basic-attributes  |feature               |
|Example  |battery part-of laptop|library has books|fan depends-on electricity|car is-a Vehicle  |baleno implements power windows|
