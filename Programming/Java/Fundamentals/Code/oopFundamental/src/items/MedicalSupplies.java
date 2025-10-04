package items;
public class MedicalSupplies extends Item {
    private int healthPointsInc;
    private String itemClass = "Medical Supplies";

    public MedicalSupplies(String name, int quantity, int healthPointsInc) {
        super(name, quantity);
        this.healthPointsInc = healthPointsInc;
    }

    public int getHealthPointsInc() {
        return healthPointsInc;
    }

    public void setCondition(int healthPointsInc) {
        this.healthPointsInc = healthPointsInc;
    }
    
    @Override
    public String toString() {
        return "Category: " + itemClass + ", Item: " + getName() + ", Quantity: " + getQuantity() + ", Health Points Increase: " + healthPointsInc;
    }
}
