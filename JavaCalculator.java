public class JavaCalculator {

    public static void main(String[] args) {

        try {

            String operation = args[0];

            if (operation.equals("sqrt")) {
                double num = Double.parseDouble(args[1]);
                System.out.println(Math.sqrt(num));
                return;
            }

            double num1 = Double.parseDouble(args[1]);
            double num2 = Double.parseDouble(args[2]);

            switch (operation) {

                case "add":
                    System.out.println(num1 + num2);
                    break;

                case "subtract":
                    System.out.println(num1 - num2);
                    break;

                case "multiply":
                    System.out.println(num1 * num2);
                    break;

                case "divide":

                    if (num2 == 0) {
                        System.out.println("Error: Cannot divide by zero");
                    } else {
                        System.out.println(num1 / num2);
                    }

                    break;

                case "power":
                    System.out.println(Math.pow(num1, num2));
                    break;

                default:
                    System.out.println("Error: Invalid operation");
            }

        } catch (Exception e) {
            System.out.println("Error: Invalid input");
        }
    }
}