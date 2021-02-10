class Solution {
    public String reformatDate(String date) {
        StringBuilder sb = new StringBuilder();
		// get the index of the first whitespace 
        int indx = date.indexOf(" ");
        
        // year is always the last 4 digits
        String year = date.substring(date.length() - 4, date.length());
        // month is always the 3 digits after the whitespace
        String month = date.substring(indx + 1, indx + 4);
        // day is always the first 3-4 chars before the whitespace
        String day = date.substring(0, indx);
		
        // append year
        sb.append(year);
        // append month
        sb.append(getMonth(month));
        // append day
        sb.append(getDay(day));
        
        return sb.toString();
    }
    
    public String getDay(String day) {
        // day is < 10
        if (day.length() == 3)
            return "0" + day.substring(0,1);
        // day is >= 10
        return day.substring(0,2);
    }
    
    public String getMonth(String month) {
        switch (month){
            case "Jan":
                return "-01-";
            case "Feb":
                return "-02-";
            case "Mar":
                return "-03-";
            case "Apr":
                return "-04-";
            case "May":
                return "-05-";
            case "Jun":
                return "-06-";
            case "Jul":
                return "-07-";
            case "Aug":
                return "-08-";
            case "Sep":
                return "-09-";
            case "Oct":
                return "-10-";
            case "Nov":
                return "-11-";
            case "Dec":
                return "-12-";
        }
        
        return "";
    }
}