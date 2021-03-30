import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;


class Main {
  public static void main(String[] args) {
    List<String> lines = new ArrayList<String>();
    Scanner stdin = new Scanner(System.in);
    while(stdin.hasNextLine()) {
      lines.add(stdin.nextLine());
    }
    stdin.close();
    double resultado_double = 0;
    int resultado_int = 0;
    Pattern pat = Pattern.compile("((\\d)+[.]((\\d)+))"); //expresion regular para identificar los decimales
    for(int i = 0; i < lines.size() ; i++){
        Matcher elemento = pat.matcher(lines.get(i)); 
        if (elemento.matches()){
            resultado_double = Double.parseDouble(lines.get(i)) + resultado_double;
        }  else {
            resultado_int = Integer.parseInt(lines.get(i)) + resultado_int;
        }
    }
    if (resultado_int == 0 ){
        System.out.println(resultado_double);
    } else if (resultado_double == 0.0){
        System.out.println(resultado_int);
    } else {
        System.out.println(resultado_double + resultado_int);
    }
  }
}