String x;
int x_len,a_index,angle,dist;
void setup() {
  Serial.begin(115200);
}

void loop() {
    if(Serial.available())
    {
      x = Serial.readString();
      x_len=x.length();
      a_index=x.indexOf('a');
      angle= x.substring(0,a_index).toInt();
      dist=x.substring(a_index+1,x_len).toInt();
      Serial.print(angle);
      Serial.print("   ");
      Serial.println(dist);
    }
}
