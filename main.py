import argparse
import alproxy
import time
import sys

from behaviour.posture import Posture
from behaviour.awareness import Awareness
from interaction.speech import Speech

from tests.behaviour import BehaviourTest

# Global variables #
DEFAULT_IP = "pepper.local"
DEFAULT_PORT = 9559

class Main:
    def __init__(self):
        self.ALProxy = alproxy.ALProxy(
                "tcp://{}:{}".format(
                    args.ip if args.ip else DEFAULT_IP,
                    args.port if args.port else DEFAULT_PORT))

        session = self.ALProxy.app.session

        self.posture = Posture(session)
        self.speech = Speech(session)
        self.awareness = Awareness(session)

    def main(self, args):
        self.ALProxy.test_all()
        self.posture.resume()
        self.awareness.resume()

    def shutdown(self):
        self.posture.stop()
        self.awareness.stop()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='UvA-Home 2018.')

    # Optional arguments
    parser.add_argument("--testbehaviour", 
                        help="Starts the tests for the behaviour class.",
                        action="store_true")
    parser.add_argument("--nosleep", 
                        help="Don't set the robot to sleep mode after termination.",
                        action="store_true")
    parser.add_argument("--ip", 
                        help="NAOqi's IP, defaults to pepper.local.")
    parser.add_argument("--port", 
                        help="NAOqi's Port, defaults to 9559.")

    args = parser.parse_args()

    try:
        main = Main()

        if args.testbehaviour:
            behaviour_test = BehaviourTest(main)
            behaviour_test.test()
        else:
            main.main(args)
            print("Done...")

    except KeyboardInterrupt:
        print "Interrupted by user, shutting down"
        if not args.nosleep:
            main.shutdown()
        sys.exit(0)
