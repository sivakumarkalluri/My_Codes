
class MoneyTransferService{
	CurrencyConverter cc=new CurrencyConverter();

int id;
 double computeTransferAmount(int index, double amount){
	 return cc.computeTransferAmount(index,amount);
	 
	 
 }
 double computeTransferFee(int index, double amount){
	 return computeTransferAmount(index,amount)*0.02;
	 
 }
 void update(MoneyTransferService s1){
	s1.id=1;
	
 }
 
 public static void main(String args[]){
	MoneyTransferService transferService = new MoneyTransferService();
	transferService.id=1000;
	transferService.update(transferService);
	System.out.println("id"+transferService.id);
	double transferAmount = transferService.computeTransferAmount(0, 1000);
	double transferFee = transferService.computeTransferFee(0, 1000);

	System.out.println("Transfer Amount: " + transferAmount);

	System.out.println("Transfer Fee: " + transferFee);
	 
 }


}
