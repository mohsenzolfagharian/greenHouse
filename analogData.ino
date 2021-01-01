
void setup() {
Serial.begin(9600);            

} 
void loop() {
  int sensor_dust = analogRead(A0);
  sensor_dust = map(sensor_dust,0,1023,100,0);
  
  int photocell = analogRead(A1);
  photocell = map(photocell,0,1023,0,100);
  
  Serial.println(photocell);
  Serial.println(sensor_dust);
}
