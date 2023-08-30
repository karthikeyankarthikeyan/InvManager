package InvManager.InvManager.models;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.hibernate.annotations.CreationTimestamp;
import org.hibernate.annotations.UpdateTimestamp;

import javax.persistence.*;
import java.sql.Timestamp;

@Entity
@Data
@Table(name = "Categories")
@AllArgsConstructor
@NoArgsConstructor
@Builder

public class Category {
    @Id
    //@GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column
    private Integer CategoryId;
    @Column
    public String categoryName;
    @Column
    private String SubcategoryName;
    @Column
    private String SubcategoryType;
    @CreationTimestamp
    @Column
    private Timestamp ModifiedAt;
    @Column
    private String ModifiedBy;


    public void setId(int CategoryId) {
        this.CategoryId= CategoryId;
    }


    }