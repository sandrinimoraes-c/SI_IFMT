import java.util.ArrayList;
import java.util.List;

public class Livro {
    private String titulo;
    private String autor;
    private String isbn;
    private List<Exemplar> exemplares;

    public Livro(String titulo, String autor, String isbn) {
        this.titulo = titulo;
        this.autor = autor;
        this.isbn = isbn;
        this.exemplares = new ArrayList<>();
    }

    public String getTitulo() {
        return titulo;
    }

    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }

    public String getAutor() {
        return autor;
    }

    public void setAutor(String autor) {
        this.autor = autor;
    }

    public String getIsbn() {
        return isbn;
    }

    public void setIsbn(String isbn) {
        this.isbn = isbn;
    }

    public void adicionarExemplar(Exemplar e) {
        this.exemplares.add(e);
    }

    public List<Exemplar> getExemplares() {
        return exemplares;
    }
}
