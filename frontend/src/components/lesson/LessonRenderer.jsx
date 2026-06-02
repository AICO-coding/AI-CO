import ConceptImage from "./ConceptImage";
import ConceptCode from "./ConceptCode";
import Parameter from "./Parameter";
import CodeFill from "./CodeFill";
import MultipleChoice from "./MultipleChoice";

const rendererMap = {
  concept_image: ConceptImage,
  concept_code: ConceptCode,
  parameter: Parameter,
  code_fill: CodeFill,
  multiple_choice: MultipleChoice,
};

export default function LessonRenderer({
  lesson,
  registerSubmit,
}) {

  if (!lesson) {
    return <div>Loading...</div>;
  }

  const Component =
    rendererMap[lesson.lessonType];

  if (!Component) {
    return (
      <div style={{ color: "red" }}>
        지원하지 않는 lesson type:
        {" "}
        {lesson.lessonType}
      </div>
    );
  }

  return (
    <Component
      lesson={lesson}
      registerSubmit={registerSubmit}
    />
  );
}