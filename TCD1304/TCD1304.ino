
#include <ADC.h>
#include <ADC_util.h>

const int readPin = A2; // ADC0 or ADC1

#define ICG 4
#define M 5
#define SH 6
#define MAX_NUM 3648

volatile uint32_t value = 0;

#if defined(ADC_TEENSY_4)
const uint32_t NUM_SAMPLES = 10000; 
#else
const uint32_t NUM_SAMPLES = 1000; 
#endif
uint32_t num_samples = NUM_SAMPLES; 
elapsedMicros timeElapsed;
volatile uint32_t num_iter = 0;


ADC *adc = new ADC(); // adc object

byte c = 9;

void clk_2MHz();
void startMeasure();


uint32_t arr[MAX_NUM];

uint32_t integration;
uint32_t n_measure;

bool stopped = false;

void setup() {
  Serial.begin(115200);
  pinMode(M, OUTPUT);
  pinMode(SH, OUTPUT);
  pinMode(ICG, OUTPUT);
  
  pinMode(readPin, INPUT_PULLUP);
  adc->adc0->enableInterrupts(adc0_isr);
  adc->adc0->setAveraging(1);
  adc->adc0->setResolution(12);
  adc->adc0->setConversionSpeed(ADC_CONVERSION_SPEED::HIGH_SPEED);
  adc->adc0->setSamplingSpeed(ADC_SAMPLING_SPEED::VERY_HIGH_SPEED);
  adc->adc0->wait_for_cal();

  num_samples = 1;

  digitalWrite(SH, LOW);
  digitalWrite(ICG, HIGH);

  value = 0;
  num_iter = 0;
  adc->adc0->startContinuous(readPin);
  while (num_iter<num_samples) {}
  adc->adc0->stopContinuous();
  Serial.println(value);

}

void loop() {

  if(Serial.available()){
    char com = Serial.read();
    if(com=='i'){
      integration=Serial.parseInt();
      Serial.write('o');
      Serial.flush();
    }
    if(com=='n'){
      n_measure=Serial.parseInt();
      Serial.write('o');
      Serial.flush();
    }
    if(com=='m'){
      
      for (int i=0; i<MAX_NUM; i++){
        arr[i] = 0;
      } 
      
      for (uint32_t j = 0; j<200; j++){
        startMeasure();
        dummy(3694);
      }
      
      for (uint32_t j = 0; j<n_measure; j++){
        delay(integration);
        startMeasure();
        dummy(32);
        read_cycle(MAX_NUM);
        dummy(14);
        Serial.write('a');
        Serial.flush();
        if (Serial.available()){
          if(Serial.read()=='s'){
            stopped=true;
            break;
          }
        }
      }

      if (stopped){
        stopped=false;
        Serial.write('s');
      } else {
        Serial.write('e');
        for (int i = MAX_NUM-1; i>=0; i--){
          sendHex(arr[i]/n_measure);
        }
        
//        for (auto val : arr){
//          sendHex(val/n_measure);
//        }
        Serial.flush();
      }
    }
  }


//  delay(10);
//  startMeasure();
//  dummy(28);
//  read_cycle(3648);
//  dummy(14);
  
} // 12 nop loop

void read_cycle(int N){
  for (int n = 0; n<N; n++){
    digitalWrite(M, HIGH);   
    for (byte i = 0;  i<3+c; i++){
      __asm__("nop"); // 3.375 ns
    }
    value = 0;                            //|
    num_iter = 0;                         //|=>  135 ns  = 29 nop
    adc->adc0->startContinuous(readPin);  //|
    
    digitalWrite(M, LOW);
    for (byte i = 0;  i<28+c; i++){ // 20+c
      __asm__("nop");
    }
    
    clk_2MHz();
    digitalWrite(M, HIGH);   
    for (byte i = 0;  i<5+c; i++){
      __asm__("nop"); // 3.375 ns
    }    
    digitalWrite(M, LOW);
    for (byte i = 0;  i<20+c; i++){ // 20+c
      __asm__("nop");
    }
    adc->adc0->stopContinuous();
    arr[n] += value;
    clk_2MHz();
  }
}

void dummy(int n){
  for (int i = 0; i<n; i++){
    clk_2MHz();
    clk_2MHz();
    clk_2MHz();
    clk_2MHz();
  }
}

void clk_2MHz(){  // c = 9
  digitalWrite(M, HIGH);
  for (byte i = 0;  i<32+c; i++){
    __asm__("nop"); // 3.375 ns
  }
  digitalWrite(M, LOW);
  for (byte i = 0;  i<28+c; i++){ // 20+c
    __asm__("nop");
  }
}

void startMeasure(){
  digitalWrite(ICG, LOW);
    clk_2MHz();
    digitalWrite(SH, HIGH);
    clk_2MHz();
    clk_2MHz();
    clk_2MHz();
    digitalWrite(SH, LOW);
    clk_2MHz();
    clk_2MHz();
    clk_2MHz();
    clk_2MHz();
    digitalWrite(ICG, HIGH);
}
void adc0_isr(void) {
    if(num_iter<num_samples) {
      value += (uint16_t)adc->adc0->analogReadContinuous();
      num_iter++;
    } else { // clear interrupt
      adc->adc0->analogReadContinuous();
    }
}

void sendHex(uint32_t n){
  Serial.print(n>>8 & 0x000F, HEX);
  Serial.print(n>>4 & 0x000F, HEX);
  Serial.print(n & 0x000F, HEX);
}
