package items;
public class Weapons extends Item {
    private int damage;
    private String type;
    private String itemClass = "Weapons";

    public Weapons(String name, int quantity, int damage, String type) {
        super(name, quantity);
        this.type = type;
        this.damage = damage;
    }

    public int getDamage() {
        return damage;
    }

    public void setDamage(int damage) {
        this.damage = damage;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    @Override
    public String toString() {
        return "Category: " + itemClass + ", Item: " + getName() + ", Quantity: " + getQuantity() + ", Damage: " + damage + ", Type: " + type;
    }
    

}
