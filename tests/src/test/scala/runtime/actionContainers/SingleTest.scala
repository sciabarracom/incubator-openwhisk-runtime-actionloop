package runtime.actionContainers


import actionContainers.ActionContainer.withContainer
import actionContainers.{ActionContainer, ActionProxyContainerTestUtils}
import common.{WskActorSystem}
import org.junit.runner.RunWith
import org.scalatest.junit.JUnitRunner
import spray.json.{JsObject}

@RunWith(classOf[JUnitRunner])
class SingleTest extends ActionProxyContainerTestUtils with  WskActorSystem {
  lazy val imageName = "actionloop-python-v3.7"

  /** indicates if strings in python are unicode by default (i.e., python3 -> true, python2.7 -> false) */
  lazy val pythonStringAsUnicode = true

  /** indicates if errors are logged or returned in the answer */
  lazy val initErrorsAreLogged = false

   def withActionContainer(env: Map[String, String] = Map.empty)(code: ActionContainer => Unit) = {
    withContainer(imageName, env)(code)
  }

  behavior of imageName

  it should "return on action error when action fails" in {
    val (out, err) = withActionContainer() { c =>
      val code =
        """
          |def div(x, y):
          |    return x/y
          |
          |def main(dict):
          |    return {"divBy0": div(5,0)}
        """.stripMargin

      val (initCode, _) = c.init(initPayload(code))
      initCode should be(200)

      val (runCode, runRes) = c.run(runPayload(JsObject()))
      /* ActionLoop does not set 502 if there are application errors
       * Since it only receive a string from the application
       * it should parse the entire string  in JSON just to find it is an "error"
       */
      if(initErrorsAreLogged)
        runCode should be(502)

      runRes shouldBe defined
      runRes.get.fields.get("error") shouldBe defined


    }
  }
}