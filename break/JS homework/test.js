var Car = function(maxSpeed, driver){
    this.maxSpeed = maxSpeed;
    this.driver = driver;
    this.drive = function(speed, time){
        console.log(speed*time);
    }
    this.logDriver = function(){
        console.log("driver name is " + this.driver)
    }
}

var myCar = new Car(24, "ninja");
var myCar2 = new Car(31, "ninja2");
var myCar3 = new Car(54, "ninja3");
var myCar4 = new Car(12, "ninja4");

myCar.drive(30,5);
myCar3.logDriver();