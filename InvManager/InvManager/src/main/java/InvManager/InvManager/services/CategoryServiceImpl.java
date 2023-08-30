package InvManager.InvManager.services;

import InvManager.InvManager.models.Category;
import InvManager.InvManager.repositories.CategoryRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
    public class CategoryServiceImpl implements CategoryService {
        private final CategoryRepository categoryRepository;

        @Autowired
        public CategoryServiceImpl(CategoryRepository categoryRepository) {

            this.categoryRepository = categoryRepository;
        }

        @Override
        //Adding a  new category

        public Category addCategory(Category category) {
            return categoryRepository.save(category);
        }

        @Override
        //Delete a category by its ID

        public void deleteCategory(int CategoryId) {
            categoryRepository.deleteById(CategoryId);
        }

        @Override
        // List all categories

        public List<Category> listAllCategories() {
            return categoryRepository.findAll();
        }

        @Override
        //update an existing category

        public Category updateCategory(int CategoryId, Category updatedCategory) {
            if (categoryRepository.existsById(CategoryId)) {
                updatedCategory.setId(CategoryId);

                return categoryRepository.save(updatedCategory);
            } else {
                throw new RuntimeException("Category not found");
            }


        }

    @Override
    public Optional<Category> searchCategory(String categoryName) {
        return categoryRepository.findByCategoryName(categoryName);
    }

//             @Override
//              public Optional<Category> searchCategoryByName(String CategoryName) {
//
//               return categoryRepository.findByCategoryName(CategoryName);

    }



        /*@Override
        //Get a total item count of a particular category

        public int getItemCount(String CategoryName){
            Optional<Category> category = categoryRepository.findByName(CategoryName);
            return category.map(Category::getItemCount).orElse(0);
        }*/


