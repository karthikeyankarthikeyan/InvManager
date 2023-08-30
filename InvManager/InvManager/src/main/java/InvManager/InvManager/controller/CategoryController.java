package InvManager.InvManager.controller;

import InvManager.InvManager.models.Category;
import InvManager.InvManager.services.CategoryService;
import org.springframework.data.repository.query.Param;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.beans.factory.annotation.Autowired;

import java.util.List;
import java.util.Optional;


@RestController
@RequestMapping("/api/v1/")

    public class CategoryController {
       @Autowired
       CategoryService categoryService;
    private CategoryService categoryservice;

    public CategoryController(CategoryService categoryService) {
            this.categoryService = categoryService;
        }

        //List all categories
        @GetMapping("/getAll")
        public ResponseEntity<List<Category>> listAllCategories() {

            return new ResponseEntity<>(categoryService.listAllCategories(), HttpStatus.OK);

        }

        // Add a new category
        @PostMapping("/Post")
        public ResponseEntity<Category> addCategory(@RequestBody Category category) {

            return new ResponseEntity<>(categoryService.addCategory(category), HttpStatus.CREATED);

        }

        // Delete a category by its ID
        @DeleteMapping({"/{CategoryId}"})
        public ResponseEntity<Category> deleteCategory(@PathVariable("CategoryId") int CategoryId) {
            categoryService.deleteCategory(CategoryId);
            return new ResponseEntity<>(HttpStatus.NO_CONTENT);
        }

        //Update an existing category
        //@Param
        //@Param
        //@Return
        @PutMapping ("/{CategoryId}")

        public <CategoryId> ResponseEntity<Category> updateCategory(@PathVariable  int CategoryId, @RequestBody Category updatedCategory) {

            try {
                Category category = categoryService.updateCategory(CategoryId, updatedCategory);

                return new ResponseEntity<>(category, HttpStatus.OK);

            } catch (RuntimeException e) {  // Catch the exception you're throwing in the service layer

                return new ResponseEntity<>(HttpStatus.NOT_FOUND);

            }

        }

        /*// Get item count for a specific category
        @GetMapping("/{CategoryName}/count")
        public ResponseEntity<Integer> getItemCount(@PathVariable int Id) {

            return new ResponseEntity<>(categoryService.getItemCount(CategoryName), HttpStatus.OK);

        }*/
        @GetMapping("/search")
        //search a category
        public ResponseEntity<Category> searchCategory(@RequestParam String categoryName) {

            Optional<Category> category = categoryService.searchCategory(categoryName);

            return category.map(ResponseEntity::ok)

                    .orElse(new ResponseEntity<>(HttpStatus.NOT_FOUND));

        }


    }


