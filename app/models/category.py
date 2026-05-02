from app.extensions import db


class Category(db.Model):
    __tablename__ = "category"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(15), nullable=False)

    questions = db.relationship("Question", back_populates="category", lazy=True)

    def __repr__(self):
        return f"<Category: {self.name}>"


