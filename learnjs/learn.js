var person={
    name: '박상영',
    age: 22,
    hello:function(name) {
        alert(this.name);
    }
}
person.hello();