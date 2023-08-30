package InvManager.InvManager.services;

import InvManager.InvManager.models.Category;
import java.util.List;
 import java.util.Optional;

public interface CategoryService {

 public Category addCategory(Category Id);

 public void deleteCategory(int CategoryId);

 public List<Category> listAllCategories();

 public Category updateCategory(int CategoryId, Category updatedCategory);

 //public int getItemCount(String CategoryName);

 public Optional<Category> searchCategory(String categoryName);


}
