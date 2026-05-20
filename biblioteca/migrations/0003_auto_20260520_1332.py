from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0002_emprestimo_data_devolucao_and_more'),
    ]

    operations = [

        migrations.RunSQL(

            sql="""
                CREATE OR REPLACE VIEW vw_emprestimos AS
                SELECT
                    e.id,
                    l.titulo AS livro,
                    u.nome AS usuario,
                    e.data_emprestimo,
                    e.data_devolucao,
                    e.devolvido
                FROM biblioteca_emprestimo e
                JOIN biblioteca_livro l
                    ON e.livro_id = l.id
                JOIN biblioteca_usuario u
                    ON e.usuario_id = u.id;
            """,

            reverse_sql="""
                DROP VIEW IF EXISTS vw_emprestimos;
            """
        ),

        migrations.RunSQL(

            sql="""
                CREATE OR REPLACE FUNCTION atualizar_disponibilidade()
                RETURNS TRIGGER AS $$
                BEGIN

                    IF NEW.devolvido = FALSE THEN

                        UPDATE biblioteca_livro
                        SET disponivel = FALSE
                        WHERE id = NEW.livro_id;

                    ELSE

                        UPDATE biblioteca_livro
                        SET disponivel = TRUE
                        WHERE id = NEW.livro_id;

                    END IF;

                    RETURN NEW;

                END;
                $$ LANGUAGE plpgsql;
            """,

            reverse_sql="""
                DROP FUNCTION IF EXISTS atualizar_disponibilidade();
            """
        ),

        migrations.RunSQL(

            sql="""
                CREATE TRIGGER trigger_emprestimo_livro

                AFTER INSERT OR UPDATE
                ON biblioteca_emprestimo

                FOR EACH ROW

                EXECUTE FUNCTION atualizar_disponibilidade();
            """,

            reverse_sql="""
                DROP TRIGGER IF EXISTS trigger_emprestimo_livro
                ON biblioteca_emprestimo;
            """
        ),
    ]