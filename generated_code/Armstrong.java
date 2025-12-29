public class Armstrong{
 public static void main(String[] args) {
 int num = 371;
 int temp = num;
 int sum = 0;
 while(temp != 0) {
 int digit = temp % 10;
 sum += Math.pow(digit, 3);
 temp /= 10;
 }
 if(sum == num)
 System.out.println("Armstrong number");
 else
 System.out.println("Not Armstrong number");
 }
}