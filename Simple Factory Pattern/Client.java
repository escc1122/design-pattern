class Client {  
    public static void main(String args[]) {  
        Chart chart;  
        String type = XMLUtil.getChartType(); //讀取配置文件中的參數  
        chart = ChartFactory.getChart(type); //創建產品對象  
        chart.display();  
    }  
}
