import java.io.*;
import com.google.gson.*;

class exec__ {
    public static void main(String[] args) throws Exception {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in, "UTF-8"));
        PrintWriter out = new PrintWriter(new OutputStreamWriter(new FileOutputStream("/dev/fd/3"), "UTF-8"));
        JsonParser json = new JsonParser();
        JsonObject error = json.parse("{\"error\":\"not an object\"}").getAsJsonObject();
        JsonObject empty = json.parse("{}").getAsJsonObject();
        String input = "";
        JsonElement output = error;
        while(true) {
            try {
                input = in.readLine();
                if(input==null)
                    break;
                JsonElement element = json.parse(input);
                if(element.isJsonObject()) {
                    JsonObject object = element.getAsJsonObject();
                    if(object.has("value")) {
                        element = object.get("value");
                        if(element.isJsonObject())
                            object = element.getAsJsonObject();
                        else object = empty.deepCopy();
                    } else {
                        object = empty.deepCopy();
                    }
                    output = main.main(object);
                } else {
                    output = error.deepCopy();
                }
                out.println(output.toString());
                out.flush();
            } catch(Exception ex) {
                ex.printStackTrace();
            }
        }
    }
}