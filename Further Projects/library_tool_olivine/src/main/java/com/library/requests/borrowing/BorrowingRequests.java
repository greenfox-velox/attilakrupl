package com.library.requests.borrowing;

import com.library.model.business.Borrowing;
import com.library.model.view.BookList;
import com.library.model.view.BookListItem;
import com.library.model.view.BorrowingList;
import com.library.model.view.BorrowingListItem;
import org.springframework.jdbc.core.JdbcTemplate;

import javax.sql.DataSource;

public class BorrowingRequests {

    JdbcTemplate template;

    public BorrowingRequests(DataSource ds) { template = new JdbcTemplate(ds); }

    public BorrowingList getAllBorrowings() {
        BorrowingList borrowingList = new BorrowingList();
        for (BorrowingListItem borrowingListItem : template.query("SELECT borrowings.borrowing_id, users.userName, books.bookTitle, borrowings.borrowingDate FROM borrowings LEFT JOIN users ON borrowings.user_id = users.user_id LEFT JOIN books ON books.book_id = borrowings.book_id", new BorrowingMapper())) {
            borrowingList.borrowings.add(borrowingListItem);
        }
        return borrowingList;
    }

    public BorrowingList getUserBorrowings(String userName) {
        BorrowingList borrowingList = new BorrowingList();
        for (BorrowingListItem borrowingListItem : template.query("SELECT borrowings.borrowing_id, users.userName, books.bookTitle, borrowings.borrowingDate FROM borrowings LEFT JOIN users ON borrowings.user_id = users.user_id LEFT JOIN books ON books.book_id = borrowings.book_id WHERE users.userName = '" + userName + "'", new BorrowingMapper())) {
            borrowingList.borrowings.add(borrowingListItem);
        }
        return borrowingList;
    }

    public void setNewBorrowing(Borrowing borrowing) {
        String SQL = "INSERT INTO borrowings (book_id, user_id, borrowingDate) VALUES (?, ?, ?)";
        template.update(SQL, borrowing.getBook_id(), borrowing.getUser_id(), borrowing.getBorrowingDate());
    }


}
