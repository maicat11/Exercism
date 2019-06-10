class ReverseString {
    String reverse(String inputString) {
        String s = "";
        for (String c : inputString.split("")) {
            s = c + s;
        }
        return s;
    }
}
